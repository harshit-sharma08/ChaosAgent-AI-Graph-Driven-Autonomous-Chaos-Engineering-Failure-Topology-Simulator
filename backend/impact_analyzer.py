import networkx as nx


def analyze_impact(graph, failed_service):
    """
    Find all services affected by a failure.
    """

    if failed_service not in graph:
        return {
            "failed_service": failed_service,
            "affected_services": [],
            "impact_count": 0
        }

    affected_services = list(
        nx.descendants(graph, failed_service)
    )

    return {
        "failed_service": failed_service,
        "affected_services": affected_services,
        "impact_count": len(affected_services)
    }