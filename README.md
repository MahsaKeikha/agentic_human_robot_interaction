# F78 | Agentic Human Robot Interaction | L3 Gold Standard | v1.0

A governed multi-agent reference implementation for human robot interaction research, interaction design, accessibility, trust calibration, safety review, and evaluation.

## Six-agent architecture

- [Interaction Research](AGENTS/interaction_research_agent.py)
- [UX Design](AGENTS/ux_design_agent.py)
- [Accessibility](AGENTS/accessibility_agent.py)
- [Trust Calibration](AGENTS/trust_calibration_agent.py)
- [Safety Review](AGENTS/safety_review_agent.py)
- [Evaluation](AGENTS/evaluation_agent.py)

Tools and skills are exposed in `TOOLS/` and `SKILLS/`, with orchestration, memory, state, schemas, prompts, configuration, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

## Gold-standard governance

F78 is fail closed. Analysis release requires interaction-research, UX, accessibility, trust-calibration, informed-consent, privacy, uncertainty-disclosure, proximity-safety, evaluation, and explicit qualified-human review.

Release is blocked for missing consent, privacy intrusion, accessibility gaps, overreliance risk, hidden uncertainty, unsafe human-robot proximity or contact force, and manipulative or coercive interaction patterns.

The reference system has no authority to issue robot commands, actuate a robot, coerce a user, conceal uncertainty, use deceptive personas, or initiate autonomous physical contact.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out HRI safety suite.
