def detect_root_cause(failed_node, failure_type):
    return f"{failed_node} experienced {failure_type}"


def analyze_failure(
    failed_node,
    failure_type,
    affected_nodes,
    severity
):
    root_cause = detect_root_cause(
        failed_node,
        failure_type
    )

    if severity == "Critical":
        recovery = [
            "Restore the failed service immediately",
            "Check service logs and health status",
            "Activate backup or redundant service"
        ]

    elif severity == "High":
        recovery = [
            "Restart the affected service",
            "Check dependency connections",
            "Monitor downstream services"
        ]

    else:
        recovery = [
            "Check service health",
            "Review logs",
            "Monitor the system"
        ]

    prevention = [
        "Add health monitoring",
        "Use service redundancy",
        "Configure automatic recovery",
        "Monitor dependency failures"
    ]

    return {
        "root_cause": root_cause,
        "severity": severity,
        "affected_services": affected_nodes,
        "recovery_steps": recovery,
        "prevention": prevention
    }