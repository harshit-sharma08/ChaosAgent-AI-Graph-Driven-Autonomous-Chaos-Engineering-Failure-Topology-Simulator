import json
import networkx as nx


def create_topology():
    graph = nx.DiGraph()

    with open("data/topology.json", "r") as file:
        data = json.load(file)

    for node in data["nodes"]:
        graph.add_node(
            node["id"],
            type=node["type"],
            criticality=node["criticality"]
        )

    for source, target in data["edges"]:
        graph.add_edge(source, target)

    return graph


def get_topology():
    graph = create_topology()

    nodes = []

    for node, data in graph.nodes(data=True):
        nodes.append({
            "id": node,
            "type": data["type"],
            "criticality": data["criticality"]
        })

    edges = []

    for source, target in graph.edges():
        edges.append({
            "source": source,
            "target": target
        })

    return {
        "nodes": nodes,
        "edges": edges
    }


def find_affected_services(graph, failed_node):
    affected = list(nx.ancestors(graph, failed_node))
    return affected


def calculate_severity(graph, failed_node):
    affected = find_affected_services(graph, failed_node)

    total_impact = len(affected)

    if graph.nodes[failed_node]["criticality"] >= 5 or total_impact >= 4:
        return "Critical"

    if total_impact >= 2:
        return "High"

    if total_impact == 1:
        return "Medium"

    return "Low"