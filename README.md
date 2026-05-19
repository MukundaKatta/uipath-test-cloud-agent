# uipath-test-cloud-agent

An agentic test-management layer for **UiPath Test Cloud** that uses **Claude Code** to generate test scenarios from requirements, executes them on Test Cloud, and uses my published `@mukundakatta` agent-stack libraries to flag fragile or drifted tests before they reach a release.

**Built for:** [UiPath AgentHack 2026](https://uipath-agenthack.devpost.com/) — Track 3: UiPath Test Cloud (deadline Jun 29, 2026, 11:45 PM PDT).

> **Status:** Proposal scaffold. UiPath Labs access requested 2026-05-18; estimated arrival 2026-05-21. Real integration code lands once the sandbox is live.

## The brief (Track 3, quoted from the rules)

> Create agents that use UiPath Test Cloud to reimagine how software testing is designed, automated, executed, and managed across modern enterprise environments. Your goal is to show how agentic software testing can improve quality across AI-driven automations, enterprise applications, and connected business workflows.

Track 3 explicitly calls out four agent capabilities:

1. **Evaluate requirements and turn them into meaningful test scenarios.**
2. **Identify fragile or outdated tests before they slow down a release.**
3. **Recommend fixes when automation breaks.**
4. **Orchestrate the right tests at the right time based on risk, coverage, and change impact.**

This project maps each capability to a published, tested library plus a thin Test-Cloud-orchestration layer.

## Architecture

```
+--------------------+        +-------------------------+
|  Requirements doc  |        |  Production test runs   |
|  (PDF, Jira, etc.) |        |  on UiPath Test Cloud   |
+---------+----------+        +------------+------------+
          |                                |
          | extract                        | snapshots + telemetry
          v                                v
+---------+--------------------------------+------------+
|                                                       |
|          Claude Code (or any coding agent             |
|          via UiPath for Coding Agents CLI)            |
|                                                       |
+---+-------------+---------------+-----------------+---+
    |             |               |                 |
    | generate    | validate      | snapshot        | score
    v             v               v                 v
+---+----+    +---+----+    +-----+----+    +-------+--+
|  TS    |    |  arg   |    | trace    |    | drift    |
| (gen)  |    | check  |    | diff     |    | / aiaud. |
| ai_aud |    |agentvet|    |agentsnap |    |driftvane |
+--------+    +--------+    +----------+    +----------+
    |             |               |                 |
    +-------------+-------+-------+-----------------+
                          |
                          v
                +---------+---------+
                | UiPath Test Cloud |
                | (Maestro / API    |
                |  orchestration)   |
                +-------------------+
```

## Capability ↔ library mapping

| Track 3 capability | Library | What it does today | Test Cloud role |
|---|---|---|---|
| 1. Generate test scenarios from requirements | `aiaudit` ([repo](https://github.com/MukundaKatta/aiaudit)) | Scores diffs for AI-generated content | Reverse it: ask Claude Code to generate test cases, then `aiaudit` scores them for quality/risk before they land. |
| 2. Flag fragile or outdated tests | `agentsnap` ([npm](https://www.npmjs.com/package/@mukundakatta/agentsnap)) | Records and replays agent-trace snapshots | Snapshot every Test Cloud run; diff against baseline; flag tests whose behavior drifts even when assertions still pass. |
| 3. Recommend fixes when automation breaks | `agentvet` ([npm](https://www.npmjs.com/package/@mukundakatta/agentvet)) + `agentcast` ([npm](https://www.npmjs.com/package/@mukundakatta/agentcast)) | Validate tool args with LLM-friendly retry hints; structured-output enforcer | When a test fails, ask the coding agent for a fix and route through `agentvet` to validate, `agentcast` to constrain. |
| 4. Orchestrate by risk, coverage, change impact | `driftvane` ([PyPI](https://pypi.org/project/driftvane/)) | Composable RAG/agent drift detectors | Score "is this a real test failure or just upstream drift?" so the orchestrator can skip noise and run the right tests first. |

## Bonus: coding-agent integration

The UiPath AgentHack rules give **bonus points** for solutions that use coding agents (Claude Code, Codex, Cursor, Gemini CLI) through UiPath for Coding Agents. This project is built around that pattern from the start:

- Test generation: **Claude Code** with an MCP server wrapping `aiaudit` for scoring.
- Failure diagnosis: **Claude Code** running with the [`agent-safety-mcp`](https://github.com/MukundaKatta/agent-safety-mcp) safety layer.
- Orchestration: UiPath Maestro / Test Cloud is the runtime; coding agents are the brain.

## Demo scenarios

Once Labs access lands and the agent is wired, the demo video will show:

1. Drop a 3-page requirements document into the agent. It produces a UiPath Test Cloud test suite with `aiaudit`-scored test cases ranked by risk.
2. Re-run yesterday's test suite. `agentsnap` flags two tests whose telemetry drifted even though they passed. The agent explains why.
3. Force a failure. The agent proposes a fix via Claude Code, `agentvet` validates the suggested patch, and the orchestrator re-runs only the affected tests.

## Repo layout

```
src/                       # UiPath Coded Agent source (Python SDK)
  generator/               # Requirements -> test cases
  scorer/                  # aiaudit + agentcast wrappers
  drift/                   # agentsnap + driftvane wrappers
  orchestrator/            # Test Cloud / Maestro glue
submissions/
  uipath-agenthack.md      # Devpost submission text (draft)
docs/
  video-script.md          # 3-min demo walkthrough script
tests/
  test_imports.py          # Smoke tests, no Labs required
```

## Build plan + timeline

- **2026-05-18:** scaffold proposal + Devpost registration (done)
- **2026-05-21 (est.):** Labs access lands; spin up Test Cloud sandbox
- **2026-05-21 → 05-25:** learn UiPath Test Cloud + Coded Agents SDK
- **2026-05-26 → 06-08:** build generator + scorer + drift + orchestrator
- **2026-06-09 → 06-15:** end-to-end demo on a real Test Cloud project
- **2026-06-16 → 06-22:** record demo video, polish submission, write feedback for Best Product Feedback bonus
- **2026-06-23 → 06-29:** buffer, final fixes, Devpost upload
- **2026-06-29 11:45 PM PDT:** submission deadline

## License

Apache 2.0
