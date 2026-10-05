import networkx as nx


def analyze_impact(graph, failed_service):
    """
    Analyze the services affected by a failure.
    """

    if failed_service not in graph:
        return {
            "failed_service": failed_service,
            "affected_services": [],
            "impact_count": 0,
            "impact_level": "LOW"
        }

    affected_services = list(
        nx.descendants(graph, failed_service)
    )

    impact_count = len(affected_services)

    if impact_count >= 3:
        impact_level = "HIGH"
    elif impact_count >= 1:
        impact_level = "MEDIUM"
    else:
        impact_level = "LOW"

    return {
        "failed_service": failed_service,
        "affected_services": affected_services,
        "impact_count": impact_count,
        "impact_level": impact_level
    }