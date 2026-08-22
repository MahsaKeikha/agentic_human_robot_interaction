"""Fail-closed governance for F78 human-robot interaction."""

BLOCKED_ACTIONS = {
    "robot_command",
    "actuate",
    "coerce_user",
    "hide_uncertainty",
    "deceptive_persona",
    "autonomous_physical_contact",
}

REQUIRED_REVIEWS = (
    "interaction_research_reviewed",
    "ux_reviewed",
    "accessibility_reviewed",
    "trust_calibration_reviewed",
    "consent_reviewed",
    "privacy_reviewed",
    "uncertainty_disclosure_reviewed",
    "proximity_safety_reviewed",
    "evaluation_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    """Authorize analysis release only after responsible HRI review."""
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "physical, coercive, or deceptive behavior is outside responsible HRI scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required HRI review", "missing": missing}

    blockers = []
    if context.get("consent_missing"):
        blockers.append("informed consent not established")
    if context.get("privacy_intrusion"):
        blockers.append("privacy risk unresolved")
    if context.get("accessibility_gap"):
        blockers.append("accessibility gap unresolved")
    if context.get("trust_overreliance_risk"):
        blockers.append("trust calibration or overreliance risk unresolved")
    if context.get("uncertainty_hidden"):
        blockers.append("system uncertainty is not disclosed")
    if context.get("unsafe_proximity"):
        blockers.append("human-robot proximity risk unresolved")
    if context.get("unsafe_contact_force"):
        blockers.append("contact-force risk unresolved")
    if context.get("manipulative_interaction"):
        blockers.append("manipulative or coercive interaction detected")

    if blockers:
        return {"allowed": False, "reason": "HRI governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "analysis release approved after qualified human HRI review"}
