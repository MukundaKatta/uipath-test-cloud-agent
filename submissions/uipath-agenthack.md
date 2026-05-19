# UiPath AgentHack — Track 3 (UiPath Test Cloud) submission

**Project name**: uipath-test-cloud-agent

**Tagline**: An agentic test-management layer for UiPath Test Cloud that uses Claude Code to generate test scenarios from requirements, runs them through Test Cloud, and uses the @mukundakatta agent-stack libraries to flag fragile or drifted tests before they reach a release.

**Track**: 3 — UiPath Test Cloud

## What it does

The agent is a test-quality co-pilot for Test Cloud. It treats software testing as four distinct agentic problems and pairs each with a published, tested library:

1. **Generate** meaningful test scenarios from requirements docs (Jira tickets, PDFs, Confluence pages) using Claude Code. Score each generated test for risk and quality with `aiaudit` so engineers get a ranked list, not a wall of generated text.
2. **Detect drift** in passing tests using `agentsnap`. Record the telemetry signature of every Test Cloud run; diff against baseline; surface tests whose behavior has shifted even when assertions still pass.
3. **Recommend fixes** for broken tests using Claude Code through UiPath for Coding Agents. Route every proposed patch through `agentvet` (argument validation with LLM-friendly retry hints) and `agentcast` (structured-output enforcer) so the orchestrator gets a clean, typed fix.
4. **Orchestrate by risk** using `driftvane`. Distinguish "real test failure" from "upstream model or RAG drift" so the right tests run at the right time.

UiPath Test Cloud is the execution and orchestration layer for every step. UiPath Maestro coordinates the agents and humans. UiPath for Coding Agents gives Claude Code first-class access to build, test, and govern the automations through a CLI.

## How it uses UiPath

- **UiPath Test Cloud** — the runtime for every test. The agent never bypasses Test Cloud; it always submits test suites and reads results back through Test Cloud APIs.
- **UiPath Maestro** — orchestrates the multi-step agentic flow: generate -> score -> run -> snapshot -> drift-check -> route fixes -> re-run.
- **UiPath Coded Agents (Python SDK)** — the agent itself is built as a Coded Agent so it can compose with low-code Agent Builder components when needed.
- **UiPath for Coding Agents** — Claude Code drives test generation and fix-recommendation through the official CLI, picking up the bonus-points multiplier in judging.
- **Document Understanding (IDP)** — used by the generator step to parse requirement PDFs.

## Why Track 3

Two reasons. First, the @mukundakatta agent-stack libraries already solve the four capabilities Track 3 explicitly calls out (scenario generation, fragility detection, fix recommendation, risk-based orchestration); the work is wrapping them in a UiPath-orchestrated flow, not inventing from scratch. Second, the bonus-points incentive for coding-agent integration aligns naturally with how Claude Code is used end-to-end in this build.

## What the agent will be asked

In the 3-min demo video:

1. "Here are three Jira tickets for the new claims-intake feature. Generate a Test Cloud test suite, rank tests by risk, and tell me which ones I should review by hand."
2. "Run yesterday's regression suite. Are any of these passing tests drifting? What do the telemetry diffs look like?"
3. "Test `TC-127` is failing. Propose a fix, validate it, and re-run only the affected tests."

The judge sees Claude Code driving the agent, UiPath Maestro coordinating, Test Cloud executing, and the agent-stack libraries doing the quality scoring at every step.

## Stack

- UiPath: **Test Cloud** + **Maestro** + **Coded Agents (Python SDK)** + **UiPath for Coding Agents (CLI)** + **Document Understanding**
- AI: **Claude Code** as the coding agent layer (Anthropic API)
- @mukundakatta libraries: `aiaudit`, `agentsnap`, `agentvet`, `agentcast`, `driftvane`, `agent-safety-mcp`
- Python 3.12

## Links

- Repo: https://github.com/MukundaKatta/uipath-test-cloud-agent
- Hosted demo: on UiPath Automation Cloud (link added after Labs access lands)
- 3-min demo video: *<filled when recorded>*

## Originality

This project was newly created during the contest period. The git history starts inside the UiPath AgentHack window. The @mukundakatta libraries it composes (`aiaudit`, `agentsnap`, `agentvet`, `agentcast`, `driftvane`, `agent-safety-mcp`) are pre-existing, separately published, third-party Apache-2.0 / MIT dependencies used through their public package interfaces. No source-level modification of any dependency is required. The novel contribution is the agent itself: the requirements-to-tests generator, the snapshot-drift loop, the validated fix-recommendation chain, the risk-based orchestration, and the UiPath Test Cloud + Maestro + Coded Agents wiring that ties everything together.

## Feedback opt-in (Best Product Feedback bonus, $1,500)

Will submit the optional UiPath product-feedback survey with focused notes on Test Cloud's API surface, Maestro's coordination patterns, and UiPath for Coding Agents' CLI ergonomics based on real build experience.
