import random


FAILURE_TYPES = [
    "Service Crash",
    "Network Failure",
    "High Latency",
    "Database Failure",
    "Timeout"
]


def select_random_node(graph):
    return random.choice(list(graph.nodes))


def select_failure_type():
    return random.choice(FAILURE_TYPES)


def inject_failure(graph, failed_node=None):

    if failed_node is None:
        failed_node = select_random_node(graph)

    if failed_node not in graph.nodes:
        raise ValueError("Service not found in topology")

    failure_type = select_failure_type()

    return {
        "failed_node": failed_node,
        "failure_type": failure_type
    }