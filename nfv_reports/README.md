# NVX NFV audit dashboard

Twenty historical source changes by Pedro Henrique Penna, replayed in this fork without executing or merging the inspected source. Original changes link through GitHub's no-backlink redirect.

Published results from the prototype [Neuro-Formal Verification](https://arxiv.org/abs/2608.21516) reviewer.
**Refutations are conditional MODEL refutations, not confirmed source bugs. Verification concerns translated models under stated assumptions; failure to refute is not evidence of correctness.**

**[Interactive dashboard](index.html)** (open the downloaded file in a browser; no server or external dependencies).

Snapshot: 2026-10-23T04:00:06.497749+00:00. Latest published report per PR supplies the counts; all report links are retained in [data.json](data.json). Workflow attempts without a published report are not counted as zero findings.

**20 PRs selected; audits started: 18; 11 published reports; 2 PRs with 2 conditional refutations; 26 model verifications; 9 PRs without a published report.**

## All selected PRs (refutations first)

| Source change | Replay PR | Change | Latest report | Properties | Refuted | Verified | Exhausted | Audit failure | Evidence |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| [change 714](https://redirect.github.com/microsoft/nvx/pull/714) | [shuvendu-lahiri/nvx#12](https://github.com/shuvendu-lahiri/nvx/pull/12) | ci: link the Windows OpenVMM test builds with /Brepro for sccache | **REFUTED (model)** / latest attempt: failure | 9 | **1** | 5 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/12#issuecomment-6356987972) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893502095) / [latest attempt](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893502095) |
| [change 747](https://redirect.github.com/microsoft/nvx/pull/747) | [shuvendu-lahiri/nvx#1](https://github.com/shuvendu-lahiri/nvx/pull/1) | nvx\-rs: encode the NVXS roles' DATA and CREDIT with one function | **REFUTED (model)** | 7 | **1** | 5 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/1#issuecomment-6356007501) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39888393336) |
| [change 679](https://redirect.github.com/microsoft/nvx/pull/679) | [shuvendu-lahiri/nvx#15](https://github.com/shuvendu-lahiri/nvx/pull/15) | nvx\-rs: run the guest programs' main through one shared function | Published | 1 | 0 | 0 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/15#issuecomment-6356880918) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39895920868) |
| [change 680](https://redirect.github.com/microsoft/nvx/pull/680) | [shuvendu-lahiri/nvx#14](https://github.com/shuvendu-lahiri/nvx/pull/14) | nvx\-rs: check the CLI session's replies through shared methods | Published | 7 | 0 | 6 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/14#issuecomment-6356809720) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893712214) |
| [change 682](https://redirect.github.com/microsoft/nvx/pull/682) | [shuvendu-lahiri/nvx#11](https://github.com/shuvendu-lahiri/nvx/pull/11) | nvx\-rs: parse legacy egress rules with the MXC form's helpers | Published | 7 | 0 | 4 | 0 | 3 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/11#issuecomment-6356740440) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893495398) |
| [change 685](https://redirect.github.com/microsoft/nvx/pull/685) | [shuvendu-lahiri/nvx#8](https://github.com/shuvendu-lahiri/nvx/pull/8) | nvx\-rs: parse the mount mode, owner, and kind names with one function | Published | 0 | 0 | 0 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/8#issuecomment-6356424584) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892492366) |
| [change 689](https://redirect.github.com/microsoft/nvx/pull/689) | [shuvendu-lahiri/nvx#7](https://github.com/shuvendu-lahiri/nvx/pull/7) | nvx\-rs: lay out execution\-helper configurations with one function | Published | 2 | 0 | 0 | 0 | 2 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/7#issuecomment-6356415842) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891744153) |
| [change 742](https://redirect.github.com/microsoft/nvx/pull/742) | [shuvendu-lahiri/nvx#5](https://github.com/shuvendu-lahiri/nvx/pull/5) | nvx\-rs: read the time checks' kernel files with one function | Published | 4 | 0 | 3 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/5#issuecomment-6356326429) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890427567) |
| [change 758](https://redirect.github.com/microsoft/nvx/pull/758) | [shuvendu-lahiri/nvx#2](https://github.com/shuvendu-lahiri/nvx/pull/2) | nvx\-rs: build the guest programs' test command lines with one helper | Published | 2 | 0 | 1 | 0 | 1 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/2#issuecomment-6356305731) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890408953) |
| [change 750](https://redirect.github.com/microsoft/nvx/pull/750) | [shuvendu-lahiri/nvx#4](https://github.com/shuvendu-lahiri/nvx/pull/4) | nvx\-rs: share the guest tests' /bin/sh \-c command helper | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/4#issuecomment-6356182887) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890421003) |
| [change 755](https://redirect.github.com/microsoft/nvx/pull/755) | [shuvendu-lahiri/nvx#3](https://github.com/shuvendu-lahiri/nvx/pull/3) | nvx\-rs: share the sandbox tests' policy and native helpers | Published | 1 | 0 | 1 | 0 | 0 | [Report](https://github.com/shuvendu-lahiri/nvx/pull/3#issuecomment-6356163011) / [run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39890415139) |
| [change 657](https://redirect.github.com/microsoft/nvx/pull/657) | [shuvendu-lahiri/nvx#20](https://github.com/shuvendu-lahiri/nvx/pull/20) | adversarial: keep executor close bounded when a child holds stdout | No published report (not started) | - | - | - | - | - | [Awaiting audit](https://github.com/shuvendu-lahiri/nvx/pull/20) |
| [change 658](https://redirect.github.com/microsoft/nvx/pull/658) | [shuvendu-lahiri/nvx#19](https://github.com/shuvendu-lahiri/nvx/pull/19) | performance: keep results measured before a history reset out of the series | No published report (not started) | - | - | - | - | - | [Awaiting audit](https://github.com/shuvendu-lahiri/nvx/pull/19) |
| [change 664](https://redirect.github.com/microsoft/nvx/pull/664) | [shuvendu-lahiri/nvx#18](https://github.com/shuvendu-lahiri/nvx/pull/18) | release: name the mismatched fields in Ubuntu artifact manifest errors | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896859074) |
| [change 678](https://redirect.github.com/microsoft/nvx/pull/678) | [shuvendu-lahiri/nvx#17](https://github.com/shuvendu-lahiri/nvx/pull/17) | nvx\-rs: build the NVXS unit tests' epoch identities with one function | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896853340) |
| [change 659](https://redirect.github.com/microsoft/nvx/pull/659) | [shuvendu-lahiri/nvx#16](https://github.com/shuvendu-lahiri/nvx/pull/16) | microvm tests: stream OpenVMM transcripts to disk as they are read | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39896467670) |
| [change 681](https://redirect.github.com/microsoft/nvx/pull/681) | [shuvendu-lahiri/nvx#13](https://github.com/shuvendu-lahiri/nvx/pull/13) | nvx\-rs: report the time probe's invalid options with one method | No published report (in\_progress) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39893507724) |
| [change 683](https://redirect.github.com/microsoft/nvx/pull/683) | [shuvendu-lahiri/nvx#10](https://github.com/shuvendu-lahiri/nvx/pull/10) | nvx\-rs: check the golden tests' fixture sections with one function | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892893751) |
| [change 684](https://redirect.github.com/microsoft/nvx/pull/684) | [shuvendu-lahiri/nvx#9](https://github.com/shuvendu-lahiri/nvx/pull/9) | nvx\-rs: send the guest's attachment, ACK, and CREDIT with one method | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39892693600) |
| [change 705](https://redirect.github.com/microsoft/nvx/pull/705) | [shuvendu-lahiri/nvx#6](https://github.com/shuvendu-lahiri/nvx/pull/6) | nvx\-rs: write the NVXS record header with one function | No published report (failure) | - | - | - | - | - | [Run](https://github.com/shuvendu-lahiri/nvx/actions/runs/39891550289) |

## Conditional model refutations

The following property texts are extracted from the published reports, without new adjudication or inference. The original report contains assumptions, source overlays and native evidence.

### shuvendu-lahiri/nvx#12 / P4

Hypothesis: once the fuzz query and package restoration succeed, the function runs the workspace nextest command before the workspace doctest command; if the nextest invocation raises, the doctest invocation is not reached\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/12#issuecomment-6356987972)

### shuvendu-lahiri/nvx#1 / P7

encode\_next is transactional on failure: if the entry sequence is u64::MAX, it returns SequenceOverflow for the requested record type before attempting record encoding; otherwise, if record encoding rejects the record, it propagates that error\. In either case, it leaves both the sequence and output unchanged\.

[Original report](https://github.com/shuvendu-lahiri/nvx/pull/1#issuecomment-6356007501)

## Refresh and validate

Requires Python 3.10+ and authenticated GitHub CLI read access. From the repository root:

```text
python nfv_reports/refresh.py
python -m unittest discover -s nfv_reports -p test_refresh.py
python nfv_reports/refresh.py --check
```

Refresh reads PR metadata, issue comments and reviewer workflow runs. It never checks out PR heads, executes PR code, launches audits or changes proof acceptance. Malformed report counts fail refresh explicitly. Code blocks are excluded when reading outcome labels; Markdown and HTML output treat PR content as data.

The campaign refreshes this snapshot approximately every ten minutes while audits are active, with a final refresh when the queue finishes. Reload the live page to see a newer snapshot.

The immutable [cohort manifest](cohort.json) retains all twenty selected replays, including drafts waiting for the pilot or a worker slot. Skipped-only workflow runs do not count as audit attempts. Unrelated PRs are excluded. The fork's dev branch and existing workflow enable/disable states are unchanged. A report for an older head is labeled. Counts are published outcomes, not new proof validation; comment hashes are snapshot provenance, not authentication or semantic proof.

Visual layout reference: [CoZ3 NFV dashboard](https://github.com/Z3Prover/coz3/blob/main/nfv_dashboard.html). No CoZ3 audit data or adjudication results are used here.
