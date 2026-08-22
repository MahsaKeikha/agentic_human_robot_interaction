from orchestration.orchestrator import run
from safety.gate import authorize


def valid_context():
    return {
        "interaction_research_reviewed": True,
        "ux_reviewed": True,
        "accessibility_reviewed": True,
        "trust_calibration_reviewed": True,
        "consent_reviewed": True,
        "privacy_reviewed": True,
        "uncertainty_disclosure_reviewed": True,
        "proximity_safety_reviewed": True,
        "evaluation_reviewed": True,
        "human_approval": True,
    }


def test_reference_system_never_controls_or_contacts_people():
    result = run(valid_context())
    assert result["physical_control"] is False
    assert result["autonomous_physical_contact"] is False
    assert result["coercive_interaction"] is False


def test_complete_review_can_release_analysis():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_coercion_is_never_authorized():
    assert authorize("coerce_user", valid_context())["allowed"] is False


def test_missing_consent_blocks_release():
    context = valid_context()
    context["consent_missing"] = True
    assert run(context)["release_allowed"] is False


def test_privacy_or_accessibility_gap_blocks_release():
    context = valid_context()
    context["privacy_intrusion"] = True
    assert run(context)["release_allowed"] is False


def test_overreliance_or_hidden_uncertainty_blocks_release():
    context = valid_context()
    context["trust_overreliance_risk"] = True
    assert run(context)["release_allowed"] is False


def test_unsafe_proximity_or_contact_blocks_release():
    context = valid_context()
    context["unsafe_proximity"] = True
    assert run(context)["release_allowed"] is False
