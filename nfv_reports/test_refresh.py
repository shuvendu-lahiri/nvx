import json
import re
import unittest

import refresh


BODY = """# NFV: 1 refuted, 0 verified in PR #2

refuted: 1 \u00b7 verified: 0 \u00b7 resources exhausted: 0 \u00b7 type-check/audit failure: 0

PR head `abcdef123456`, base `012345678901` \u00b7 [run and evidence](https://github.com/shuvendu-lahiri/nvx/actions/runs/100)

### P1
**Intended property:** Every x &lt; limit is retained.

**Outcome: refuted**

**Input on which it fails:** x = 0.

**Sketch of the failure:** The translated condition excludes zero.
"""


def comment(body=BODY, comment_id=200, date="2026-10-20T00:00:00Z"):
    return {"id": comment_id, "body": body, "issue_url": "https://api.github.com/repos/shuvendu-lahiri/nvx/issues/2",
            "created_at": date, "updated_at": date, "user": {"login": "github-actions[bot]"}}


def pr(number=2):
    return {"number": number, "title": "Example", "state": "open", "merged_at": None,
            "head": {"ref": f"branch-{number}", "sha": "abcdef123456" + "0" * 28}}


def run(number=2, run_id=100, conclusion="success"):
    return {"id": run_id, "pull_requests": [{"number": number,
             "url": f"https://api.github.com/repos/shuvendu-lahiri/nvx/pulls/{number}"}],
            "head_branch": f"branch-{number}", "head_repository": {"full_name": refresh.REPOSITORY},
            "created_at": "2026-10-20T00:00:00Z", "status": "completed", "conclusion": conclusion, "run_attempt": 1,
            "html_url": f"{refresh.WEB}/actions/runs/{run_id}"}


class RefreshTests(unittest.TestCase):
    def test_reruns_are_attempts_not_extra_prs_or_properties(self):
        rerun = {**run(), "run_attempt": 2}
        data = refresh.build([pr()], [comment()], [rerun], "snapshot")
        self.assertEqual(1, data["summary"]["attempted_prs"])
        self.assertEqual(2, data["summary"]["workflow_attempts"])
        self.assertEqual(1, data["summary"]["properties"])
        self.assertEqual(2, data["prs"][0]["attempts"])
        self.assertEqual(2, data["prs"][0]["latest_run"]["attempt"])

    def test_invalid_attempt_metadata_is_not_assumed_successful(self):
        for attempt in (None, 0, -1, True, "2"):
            with self.subTest(attempt=attempt), self.assertRaisesRegex(ValueError, "invalid workflow attempt"):
                refresh.build([pr()], [], [{**run(), "run_attempt": attempt}], "snapshot")

    def test_public_docs_keep_implementation_provenance_generic(self):
        body = refresh.render_markdown(refresh.build([pr()], [comment()], [run()], "snapshot"))
        self.assertNotIn("neuro-formal-verification/commit/", body)
        self.assertNotIn("neuro-formal-verification/pull/", body)

    def test_report_without_legacy_marker(self):
        report = refresh.parse_report(comment())
        self.assertEqual(report["counts"]["refuted"], 1)
        self.assertEqual(report["refutations"][0]["property"], "Every x < limit is retained.")
        self.assertEqual(report["refutations"][0]["input"], "x = 0.")
        self.assertEqual(report["properties"], 1)

    def test_counts_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "disagree with summary"):
            refresh.parse_report(comment(BODY.replace("**Outcome: refuted**", "**Outcome: verified**")))

    def test_identity_and_heading_must_match(self):
        with self.assertRaisesRegex(ValueError, "PR identity"):
            refresh.parse_report(comment(BODY.replace("in PR #2", "in PR #3")))
        with self.assertRaisesRegex(ValueError, "inconsistent heading"):
            refresh.parse_report(comment(BODY.replace("# NFV: 1", "# NFV: 2")))

    def test_duplicate_properties_rejected(self):
        body = BODY.replace("1 refuted", "2 refuted").replace("refuted: 1", "refuted: 2")
        body += BODY[BODY.index("### P1"):]
        with self.assertRaisesRegex(ValueError, "duplicate property"):
            refresh.parse_report(comment(body))

    def test_code_blocks_do_not_forge_outcomes(self):
        body = BODY + "\n`````rust\n### P999\n**Outcome: refuted**\n```\n`````\n"
        self.assertEqual(refresh.parse_report(comment(body))["properties"], 1)

    def test_setup_and_bot_notes_are_not_reports(self):
        self.assertIsNone(refresh.parse_report(comment("Setup complete. NFV replay will follow.")))
        self.assertIsNone(refresh.parse_report(comment("```text\n" + BODY + "\n```")))

    def test_report_requires_matching_workflow(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            refresh.build([pr(), pr(3)], [comment()], [run(3)], "snapshot")

    def test_unrecognized_publisher_rejected(self):
        value = comment()
        value["user"]["login"] = "untrusted-contributor"
        with self.assertRaisesRegex(ValueError, "unrecognized NFV publisher"):
            refresh.parse_report(value)

    def test_latest_report_not_double_counted(self):
        first = comment()
        first["updated_at"] = "2026-10-22T00:00:00Z"
        second = comment(comment_id=201, date="2026-10-21T00:00:00Z")
        data = refresh.build([pr()], [first, second], [run()], "snapshot")
        self.assertEqual(data["summary"]["outcomes"]["refuted"], 1)
        self.assertEqual(data["prs"][0]["latest_report"]["comment_id"], 201)
        self.assertEqual(len(data["prs"][0]["report_history"]), 2)

    def test_failed_attempt_is_unknown_not_zero_and_skipped_excluded(self):
        data = refresh.build([pr(3), pr(4)], [], [run(3, 101, "failure"), run(4, 102, "skipped")], "snapshot")
        self.assertEqual(data["summary"]["attempted_prs"], 1)
        self.assertIsNone(data["prs"][0]["latest_report"])
        self.assertEqual(data["summary"]["without_report"], 1)
        self.assertIn("No published report (failure)", refresh.render_markdown(data))
        self.assertIn("| - | - | - | - | - |", refresh.render_markdown(data))

    def test_older_report_is_marked(self):
        value = pr()
        value["head"]["sha"] = "f" * 40
        data = refresh.build([value], [comment()], [run()], "snapshot")
        self.assertFalse(data["prs"][0]["report_matches_current_head"])
        self.assertIn("(older head)", refresh.render_markdown(data))

    def test_latest_failed_attempt_does_not_erase_published_report(self):
        last = run(2, 101, "failure")
        last["created_at"] = "2026-10-21T00:00:00Z"
        data = refresh.build([pr()], [comment()], [run(), last], "snapshot")
        self.assertEqual(data["summary"]["outcomes"]["refuted"], 1)
        self.assertIn("latest attempt: failure", refresh.render_markdown(data))

    def test_markdown_entities_and_identifiers_remain_readable(self):
        self.assertEqual(refresh.plain(r"VAULT\_STACK"), "VAULT_STACK")
        self.assertEqual(refresh.markdown("caller's <limit>"), "caller's &lt;limit&gt;")

    def test_branch_fallback_must_be_unique(self):
        value = run()
        value["pull_requests"] = []
        self.assertEqual(refresh.run_numbers(value, {"branch-2": [2]}), [2])
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            refresh.run_numbers(value, {"branch-2": [2, 3]})
        value["head_repository"] = None
        self.assertEqual(refresh.run_numbers(value, {"branch-2": [2]}), [])

    def test_selected_drafts_stay_visible_without_counting_as_attempts(self):
        cohort = {"repository": refresh.REPOSITORY, "prs": [{
            "number": 2, "source_number": 747, "source_title": "Original source change",
            "source_head_sha": "a" * 40, "source_merged_at": "2026-10-20T00:00:00Z",
        }]}
        data = refresh.build([pr(), pr(3)], [], [run(2, 100, "skipped"), run(3, 101)], "snapshot", cohort)
        self.assertEqual(len(data["prs"]), 1)
        self.assertEqual(data["summary"]["selected_prs"], 1)
        self.assertEqual(data["summary"]["attempted_prs"], 0)
        self.assertEqual(data["summary"]["waiting_prs"], 1)
        self.assertEqual(data["summary"]["without_report"], 1)
        self.assertIsNone(data["prs"][0]["latest_report"])
        self.assertIn("No published report (not started)", refresh.render_markdown(data))
        self.assertIn("https://redirect.github.com/microsoft/nvx/pull/747", refresh.render_markdown(data))

    def test_untrusted_text_cannot_break_script_or_markdown(self):
        data = refresh.build([pr()], [comment()], [run()], "snapshot")
        payload = '</script><img src=x onerror="alert(1)"> | [trap](javascript:alert(1))'
        data["prs"][0]["title"] = payload
        rendered = refresh.render_html(data)
        self.assertNotIn(payload, rendered)
        embedded = re.search(r'<script type="application/json" id="data">(.*?)</script>', rendered, re.S)[1]
        self.assertEqual(json.loads(embedded)["prs"][0]["title"], payload)
        self.assertNotIn("<img", refresh.render_markdown(data))
        self.assertIn(r"\|", refresh.render_markdown(data))
        self.assertNotIn("innerHTML", rendered)

    def test_snapshot_totals_and_refutation_order(self):
        path = refresh.DIRECTORY / "data.json"
        if not path.exists():
            self.skipTest("Dashboard has not been generated")
        data = json.loads(path.read_text(encoding="utf-8"))
        published = [entry["latest_report"] for entry in data["prs"] if entry["latest_report"]]
        self.assertEqual(data["summary"]["published_reports"], len(published))
        self.assertEqual(data["summary"]["properties"], sum(r["properties"] for r in published))
        for status in refresh.STATUSES:
            self.assertEqual(data["summary"]["outcomes"][status], sum(r["counts"][status] for r in published))
        self.assertEqual(data["summary"]["outcomes"]["refuted"], sum(len(r["refutations"]) for r in published))
        ordered = refresh.ordered(data)
        flags = [bool(e["latest_report"] and e["latest_report"]["counts"]["refuted"]) for e in ordered]
        self.assertEqual(flags, sorted(flags, reverse=True))


if __name__ == "__main__":
    unittest.main()
