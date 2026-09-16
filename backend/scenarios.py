SCENARIOS = {
    "database_failure": {
        "name": "Database Failure",
        "node": "Database",
        "failure_type": "Database Failure"
    },

    "payment_failure": {
        "name": "Payment Service Failure",
        "node": "Payment Service",
        "failure_type": "Service Crash"
    },

    "api_failure": {
        "name": "API Gateway Failure",
        "node": "API Gateway",
        "failure_type": "Network Failure"
    },

    "order_failure": {
        "name": "Order Service Failure",
        "node": "Order Service",
        "failure_type": "Service Crash"
    }
}


def get_scenarios():
    return SCENARIOS