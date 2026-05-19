# 3-min demo script

A draft narration outline. Final video lands once Labs access is live and the agent is wired.

## 0:00 — 0:25 (Cold open, problem)

> Show three Jira tickets in a sidebar. Voice over: "Three tickets, one feature, a hundred edge cases nobody's testing. The cost of missing those isn't the bug — it's finding out in production. So I built an agent that turns these tickets into a Test Cloud suite, ranks the suite by risk, runs it, watches for drift, and routes fixes when something breaks."

## 0:25 — 0:55 (Test generation, Track 3 capability #1)

> Drag the three Jira tickets into the agent's chat. Claude Code spins up under UiPath for Coding Agents. The agent reads the tickets, generates a test suite, and `aiaudit` scores each test. A ranked list appears: 3 high-risk, 4 medium, 5 low. Voice over: "Every test gets a confidence score from `aiaudit`. The high-risk ones are exactly the cases a human reviewer should look at first."

## 0:55 — 1:30 (Drift detection, capability #2)

> Show yesterday's passing run vs. today's passing run. Both green. Then run `agentsnap` diff. Two tests are flagged. Voice over: "Both runs pass. But two tests have drifted — their telemetry signature shifted. `agentsnap` catches it because it records traces, not just assertions. The orchestrator flags them as fragile before they break in production."

## 1:30 — 2:05 (Failure + fix, capability #3)

> Inject a failure in test `TC-127`. The agent runs Claude Code to propose a fix. `agentvet` validates the proposed patch. `agentcast` formats the fix as a structured response. Voice over: "Claude Code reads the failure, proposes a patch, `agentvet` checks the args, `agentcast` enforces the schema. Maestro routes the fix through human review and re-runs only the affected tests."

## 2:05 — 2:30 (Orchestration, capability #4)

> Show the Maestro flow handling risk-based orchestration. `driftvane` distinguishes "test broke" from "upstream model drifted." Voice over: "When a model upstream of the test drifts, `driftvane` tells the orchestrator not to chase it as a test failure. The right tests run at the right time."

## 2:30 — 2:50 (Stack summary)

> Quick montage of the stack. Voice over: "All of this runs on UiPath Test Cloud, orchestrated by Maestro, driven by Claude Code through UiPath for Coding Agents, with @mukundakatta libraries doing the quality scoring at every step."

## 2:50 — 3:00 (Close)

> Final slide with repo + Test Cloud URL. Voice over: "Code's at github.com/MukundaKatta/uipath-test-cloud-agent. Apache 2.0."
