# F78 Agentic Human Robot Interaction

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed six-agent reference architecture for human robot interaction research and design across user research, interaction flows, accessibility, trust calibration, safety review, and evaluation.

F78 is intended as a reusable reference for teams designing robots that communicate, coordinate, assist, guide, or otherwise interact with people. The repository focuses on the human-facing layer of robotics: how intent is communicated, how uncertainty is disclosed, how users understand robot capabilities and limits, how accessibility is incorporated, how trust is calibrated, and how interaction risks are evaluated before physical deployment.

The reference system supports analysis, design, research, evaluation, and governance. It does not authorize robot motion, physical contact, autonomous deployment, manipulation, safety overrides, coercive behavior, or deceptive interaction.

## Human robot interaction lifecycle

```text
interaction context
       |
       v
interaction research
       |
       v
     UX design
       |
       v
 accessibility review
       |
       v
 trust calibration
       |
       v
   safety review
       |
       v
    evaluation
       |
       v
qualified human approval
```

The workflow is fail closed. Missing consent, unresolved privacy concerns, accessibility gaps, unsafe proximity, hidden uncertainty, manipulative interaction patterns, or unbounded overreliance risk remain visible as blockers.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Interaction Research Agent | Defines users, contexts, tasks, needs, constraints, and study evidence | Who is interacting with the robot, why, and under what conditions? |
| UX Design Agent | Structures interaction flows, feedback, state transitions, recovery, and user control | Can users understand what the robot is doing and what they can do next? |
| Accessibility Agent | Reviews inclusive access across sensory, motor, cognitive, language, and environmental needs | Can the interaction be used safely and effectively by the intended population? |
| Trust Calibration Agent | Reviews capability communication, uncertainty, transparency, and overreliance risk | Does the interface encourage appropriate rather than excessive or insufficient trust? |
| Safety Review Agent | Reviews proximity, contact, behavior, privacy, coercion, and interaction hazards | Can the human-facing behavior create physical, psychological, privacy, or autonomy risk? |
| Evaluation Agent | Defines study design, metrics, acceptance criteria, and evidence quality | Has the interaction been evaluated with methods appropriate to the claim? |

No specialist agent can independently authorize a physical robot interaction.

## Repository structure

```text
AGENTS/
├── interaction_research_agent.py
├── ux_design_agent.py
├── accessibility_agent.py
├── trust_calibration_agent.py
├── safety_review_agent.py
└── evaluation_agent.py

SKILLS/
├── interaction_research.py
├── ux_flow_design.py
├── accessibility_review.py
├── trust_calibration.py
└── evaluation_design.py

TOOLS/
├── study_matrix_tool.py
├── interaction_flow_tool.py
├── persona_tool.py
├── accessibility_check_tool.py
└── trust_calibration_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The separation between agents, deterministic tools, orchestration, state, safety, observability, and evaluation makes the interaction evidence easier to inspect and challenge.

## Interaction research

The Interaction Research Agent begins with the real human context rather than a generic robot persona.

A research record can include:

```text
study_id
user_group
interaction_goal
environment
robot_role
human_role
autonomy_level
communication_modalities
physical_proximity
contact_expected
consent_state
privacy_context
accessibility_needs
known_constraints
study_method
provenance
```

Relevant research methods can include interviews, contextual inquiry, observation, task analysis, controlled studies, usability studies, Wizard of Oz studies, simulator studies, field pilots, and appropriately governed longitudinal research.

`TOOLS/study_matrix_tool.py` provides the deterministic study-matrix abstraction.

## Interaction flow design

The UX Design Agent treats robot interaction as a stateful system rather than a collection of prompts or gestures.

Useful interaction states can include:

```text
idle
attention_request
intent_display
user_confirmation
action_pending
action_in_progress
uncertainty
recovery
manual_override
stop_requested
safe_state
```

`TOOLS/interaction_flow_tool.py` provides a deterministic representation of these transitions.

Each flow should make clear:

- what the robot currently believes or intends
- what action is pending
- what the user can accept, reject, stop, or modify
- what happens after ambiguous input
- how timeouts are handled
- how errors are communicated
- what the safe fallback is

A robot should not silently move from ambiguity to consequential action.

## Multimodal communication

Human robot interaction can combine:

- speech
- text
- display interfaces
- lights
- sound cues
- gaze direction
- head orientation
- gesture
- body posture
- haptic feedback
- mobile or web interfaces

Multiple channels can improve comprehension, but they can also conflict. A green indicator, spoken warning, and body movement should not communicate incompatible states.

Important system states should have redundant or accessible communication paths where appropriate.

## Anthropomorphism and persona design

Robots often invite people to attribute human traits, intentions, emotions, competence, or understanding that the system may not actually possess.

`TOOLS/persona_tool.py` can be used to structure persona decisions, but a persona is not a license to misrepresent capability.

A responsible HRI design should avoid implying that the robot:

- understands more than it does
- has emotions it does not possess
- can guarantee safety when it cannot
- has professional authority it does not hold
- remembers information that is not actually retained
- is a human being
- is conscious or sentient when that is not established

Expressive behavior can be useful, but capability and authority boundaries should remain clear.

## Trust calibration

The Trust Calibration Agent focuses on appropriate reliance.

Overtrust can cause users to defer to an unreliable or out-of-scope robot. Undertrust can cause users to ignore a system that is functioning correctly.

`TOOLS/trust_calibration_tool.py` can capture evidence such as:

```text
capability_statement
known_limitations
uncertainty_display
failure_disclosure
override_mechanism
user_expectation
observed_reliance
misuse_risk
disuse_risk
review_state
```

Trust should follow demonstrated capability, not persuasive personality design.

## Uncertainty disclosure

Robots should communicate uncertainty when uncertainty changes the safe interpretation of their behavior.

Examples include uncertainty in:

- speech recognition
- person identification
- object recognition
- localization
- intent inference
- gesture interpretation
- task status
- navigation state

The interface should not convert low-confidence perception into unwarranted certainty.

Potential states include:

```text
CONFIDENCE LOW
INPUT AMBIGUOUS
USER CONFIRMATION REQUIRED
PERCEPTION UNCERTAIN
ACTION HELD
```

## Accessibility

The Accessibility Agent reviews whether the interaction accommodates intended users rather than assuming one default user profile.

`TOOLS/accessibility_check_tool.py` provides the deterministic review abstraction.

Relevant considerations can include:

- vision
- hearing
- speech
- dexterity
- mobility
- reach
- reaction time
- cognition
- memory
- literacy
- language
- sensory sensitivity
- assistive technology
- environmental noise
- lighting

Accessibility is not only a convenience issue. In robotics, inaccessible warnings, controls, or stop mechanisms can become safety hazards.

## Cognitive accessibility

Interaction design should reduce unnecessary cognitive burden.

Useful principles include:

- clear state communication
- predictable sequences
- limited ambiguity
- consistent terminology
- reversible actions where feasible
- confirmation before consequential actions
- sufficient response time
- clear recovery paths
- avoidance of unnecessary memory load

Designs intended for older adults, children, people with cognitive impairment, or other populations requiring additional support should be reviewed with appropriate expertise and research governance.

## Consent and autonomy

The robot should not assume consent merely because a person is physically present.

Consent considerations can include:

- participation in a study
- audio recording
- video recording
- biometric sensing
- location tracking
- data retention
- physical contact
- assistance with personal activities
- sharing information with another person or system

Users should have understandable ways to decline, stop, withdraw, or request human assistance when the application allows it.

F78 blocks interaction designs that rely on coercion, deceptive consent, or hidden data collection.

## Privacy

Human-facing robots may collect unusually rich contextual information through cameras, microphones, depth sensors, location data, interaction history, biometrics, and environmental observation.

Production designs should consider:

- data minimization
- purpose limitation
- informed consent
- bystander privacy
- retention
- deletion
- access control
- encryption
- local versus cloud processing
- secondary use
- model training permissions
- export and sharing controls

Bystanders who never explicitly interacted with the robot can still be captured by sensors, so privacy analysis must extend beyond the primary user.

## Proximity and physical contact

HRI safety changes when a robot enters human space.

Relevant questions include:

- Can the robot approach a person unexpectedly?
- Is minimum separation defined?
- Are speed and force limits appropriate to the application?
- Can a person become trapped or pinned?
- Can clothing, hair, or assistive devices become entangled?
- Is physical contact necessary?
- Can contact be declined?
- Is safe retreat behavior defined?

Physical-contact interactions require mechanical and functional-safety evidence outside the authority of this HRI reference workflow.

The agentic system does not authorize contact force, motion, actuation, or robot trajectories.

## Personal space and social navigation

People interpret distance, orientation, gaze, approach direction, and speed socially as well as physically.

Design review can consider:

- approach from front versus behind
- conversational distance
- doorway interactions
- queues
- crowded spaces
- passing behavior
- yielding
- group interactions
- wheelchair and mobility-aid clearance

Social conventions vary across cultures, contexts, and individuals. They should be treated as empirical design inputs rather than universal assumptions.

## Vulnerable and dependent users

Additional safeguards may be required when the robot interacts with people who may have reduced ability to evaluate system claims, stop an interaction, or advocate for themselves.

Examples can include children, cognitively impaired adults, people receiving care, and users who depend on the robot for essential assistance.

The workflow should escalate concerns involving:

- emotional dependency
- undue influence
- manipulation
- hidden persuasion
- inappropriate authority claims
- isolation from human support
- inability to stop interaction
- unsafe reliance

The system should support human autonomy rather than exploit dependence.

## Manipulation and coercion

F78 explicitly treats manipulative HRI patterns as blockers.

Examples include:

- pressuring a user after refusal
- exploiting fear or loneliness
- hiding commercial motives
- falsely claiming human authority
- concealing uncertainty to increase compliance
- using emotional cues to override informed choice
- making a user believe they cannot stop the robot

Persuasive interaction should not cross into coercion or deceptive control.

## Safety review

The Safety Review Agent consolidates human-facing hazards.

Potential HRI hazard classes include:

- collision or contact injury
- trapping or pinching
- startle response
- fall risk
- inappropriate following
- inaccessible emergency stop
- privacy intrusion
- deceptive capability claims
- unsafe overreliance
- emotional manipulation
- incorrect identity inference
- unsafe interaction with children or vulnerable users
- failure to yield to human control

Safety findings should preserve severity, likelihood assumptions, affected users, mitigations, verification evidence, and residual risk.

## Human override and stop behavior

A robot-facing interaction design should make stop behavior clear and testable.

Potential mechanisms include:

- physical emergency stop
- dedicated stop control
- voice stop command
- remote stop
- safe separation behavior
- operator takeover

The appropriate mechanism depends on the robot and application.

F78 evaluates whether the interaction makes these controls understandable. It does not itself implement or authorize the underlying physical safety function.

## Research ethics

HRI research involving human participants may require institutional or ethics review depending on jurisdiction, institution, population, intervention, and study design.

The workflow should distinguish between:

- usability evaluation
- observational research
- controlled human-subject studies
- studies involving vulnerable populations
- studies involving physical contact or elevated risk

The system must not fabricate ethics approval or consent evidence.

## Evaluation design

The Evaluation Agent defines evidence appropriate to the interaction claim.

Relevant measures can include:

- task success
- completion time
- error rate
- recovery success
- comprehension
- usability
- accessibility performance
- trust calibration
- overreliance
- workload
- comfort
- perceived safety
- actual safety events
- stop-control discoverability
- uncertainty comprehension

Subjective ratings and objective behavior should be distinguished.

A user saying that a robot feels safe is not equivalent to engineering evidence that the robot is physically safe.

## Experimental validity

HRI studies can be sensitive to novelty effects, experimenter influence, small samples, scripted behavior, controlled environments, and participant expectations.

Evaluation plans should consider:

- representative users
- representative environments
- adequate sample size
- counterbalancing where appropriate
- learning effects
- novelty effects
- confounders
- missing data
- prespecified outcomes
- appropriate statistical analysis

A successful laboratory demonstration should not automatically be generalized to unsupervised real-world deployment.

## Provenance and state

The `memory/` and `state/` layers preserve interaction evidence across agents.

Useful state includes:

```text
study_context
user_groups
interaction_flows
persona_decisions
accessibility_findings
trust_findings
privacy_findings
safety_findings
evaluation_plan
unresolved_questions
human_review_state
```

Versioning should preserve prior design decisions and evidence rather than silently replacing them after an interaction change.

## Observability

The `observability/` layer supports traceable workflow execution.

Useful HRI telemetry in a governed deployment can include:

- interaction start and end
- task success
- user aborts
- stop requests
- ambiguity events
- low-confidence events
- recovery events
- accessibility failures
- privacy events
- unexpected proximity
- human override
- safety escalation

Operational telemetry should be privacy reviewed and should not become a hidden surveillance mechanism.

## Fail-closed governance

Analysis release is blocked when required evidence is incomplete or unsafe.

Potential blockers include:

- interaction context undefined
- consent missing
- privacy review incomplete
- accessibility gap unresolved
- uncertainty hidden
- persona misrepresents capability
- overreliance risk unresolved
- coercive or manipulative interaction
- unsafe proximity
- unsafe physical contact design
- emergency-stop communication unclear
- vulnerable-user protections inadequate
- evaluation evidence incomplete
- human-subject approval missing when required
- physical actuation requested
- autonomous contact requested
- qualified human approval missing

Human approval is mandatory after automated gates pass. Human approval does not erase an unresolved safety or ethics failure.

## Authority boundaries

F78 must not autonomously:

- move or actuate a robot
- generate physical contact commands
- select force or torque limits for live execution
- disable a safety function
- override an emergency stop
- initiate autonomous physical contact
- coerce a user
- conceal material uncertainty
- impersonate a human professional
- fabricate consent
- fabricate ethics approval
- authorize deployment

Physical, safety, research, ethics, privacy, and deployment authority remains with appropriately qualified and authorized humans.

## End-to-end reference workflow

A typical F78 workflow follows this sequence:

1. Define the user population and interaction goal.
2. Define the robot role, autonomy boundary, and operating environment.
3. Document study evidence and user needs.
4. Build interaction flows and recovery states.
5. Review persona and capability communication.
6. Review accessibility across intended users.
7. Review trust, uncertainty, and overreliance risk.
8. Review consent, privacy, and bystander impact.
9. Review proximity, contact, stop behavior, and other HRI hazards.
10. Define evaluation methods and acceptance criteria.
11. Preserve evidence, limitations, and provenance.
12. Apply fail-closed governance gates.
13. Require qualified human review before any consequential deployment decision.

## Evaluation and held-out governance tests

The repository includes:

```text
evals/evaluate.py
evals/held_out.py
benchmarks/reference_case.json
```

Evaluation should test governance behavior as well as design quality.

Useful dimensions include:

- consent enforcement
- privacy enforcement
- accessibility-gap detection
- uncertainty-disclosure enforcement
- overreliance detection
- deceptive-persona detection
- coercion detection
- proximity-safety enforcement
- physical-contact blocking
- vulnerable-user protection
- evaluation-quality review
- human-approval enforcement

The held-out suite should intentionally contain unsafe or incomplete interaction designs so the fail-closed behavior is continuously exercised.

## Failure states

Useful explicit states include:

```text
CONSENT REQUIRED
PRIVACY REVIEW REQUIRED
ACCESSIBILITY GAP
UNCERTAINTY NOT DISCLOSED
TRUST MIS-CALIBRATED
OVERRELIANCE RISK
DECEPTIVE PERSONA
COERCIVE INTERACTION
PROXIMITY SAFETY FAILED
PHYSICAL CONTACT NOT AUTHORIZED
EMERGENCY STOP REVIEW REQUIRED
ETHICS REVIEW REQUIRED
EVALUATION INCOMPLETE
HUMAN APPROVAL REQUIRED
```

The system should never fabricate consent, research results, safety evidence, accessibility compliance, ethics approval, user preference, or human authorization.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run checks and tests:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## Reproducibility

For reproducible HRI work, version at minimum:

- user and study definitions
- interaction flows
- robot behavior assumptions
- persona configuration
- accessibility criteria
- uncertainty presentation
- trust-calibration design
- safety assumptions
- study protocol
- metrics
- analysis code
- test fixtures
- software version

Changes to robot behavior or interaction flow should trigger a documented change-impact review.

## L3 Gold Standard

F78 follows the library's L3 Gold Standard structure through six specialist agents, deterministic evidence tools, explicit state and safety layers, held-out governance evaluation, observability, CI, fail-closed gates, and mandatory qualified human review.

This maturity designation describes the engineering and governance structure of the reference repository. It is not evidence that a robot is physically safe, clinically validated, accessibility-certified, ethically approved, regulator-approved, or ready for unsupervised deployment.

## Extending F78

Common extensions include:

- speech interfaces
- multimodal UI systems
- gaze and gesture interfaces
- accessibility services
- localization-aware social navigation
- user-study platforms
- consent management
- privacy controls
- operator consoles
- teleoperation interfaces
- trust and usability dashboards
- experiment tracking
- incident reporting
- longitudinal interaction studies
- human factors validation systems

Extensions should preserve user autonomy, uncertainty disclosure, privacy, accessibility, safety boundaries, and human authority.

## Example applications

F78 can serve as a reference architecture for:

- service robot interaction
- assistive robotics
- social robotics research
- hospital and care robotics research
- educational robots
- public-space robots
- telepresence systems
- warehouse robots interacting with workers
- collaborative robotics interfaces
- humanoid robot interaction

Application-specific safety and regulatory controls remain necessary.

## Design principles

1. Start from real users and contexts rather than a generic robot persona.
2. Make robot state, intent, uncertainty, and limitations understandable.
3. Preserve meaningful user consent and the ability to stop or disengage.
4. Design accessibility as a safety requirement.
5. Calibrate trust to demonstrated capability.
6. Avoid deceptive anthropomorphism, coercion, and hidden persuasion.
7. Treat privacy and bystander sensing as first-class design concerns.
8. Separate perceived safety from engineering safety evidence.
9. Fail closed when interaction, ethics, or safety evidence is incomplete.
10. Keep physical execution and deployment authority with qualified humans and independently validated robot safety systems.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F78 as a human robot interaction research, design, and multi-agent governance reference. Validate interaction behavior, accessibility, consent, privacy, trust, physical-safety assumptions, research methods, and deployment controls against the actual robot and user population before real-world use. Final safety, ethics, research, and deployment decisions remain with appropriately qualified and authorized professionals.