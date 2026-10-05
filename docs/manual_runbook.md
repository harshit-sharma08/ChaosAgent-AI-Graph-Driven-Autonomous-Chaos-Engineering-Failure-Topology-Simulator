# Manual Baseline Runbook — ChaosAgent AI

This document provides instructions for collecting baseline recovery and impact data for controlled failure simulations performed in **ChaosAgent AI**.

ChaosAgent AI uses a dependency graph to simulate service failures and analyze how the failure propagates through connected services. The experiments described below are **controlled simulations** and do not intentionally disrupt real production infrastructure.

---

## 1. Prerequisites

Before running the experiments:

1. ChaosAgent AI should be running locally.
2. A valid service topology should be available.
3. Services/nodes should have valid dependency relationships.
4. The Graph Engine should be available for failure propagation analysis.
5. The experiment dashboard should be accessible.
6. The experiment result/history storage should be available if enabled.
7. AI/LLM integration should be configured if AI explanation is being tested.

---

## 2. Baseline Conditions

Before starting an experiment:

1. Open the ChaosAgent AI dashboard.
2. Confirm that the topology is loaded correctly.
3. Verify that all simulated services are in a **Healthy** state.
4. Confirm that no previous failure simulation is active.
5. Record the initial topology/state.
6. Select the service that will be used as the failure target.

---

## 3. Experiment Flow

For every experiment:

1. **Select a service** from the topology.
2. **Select a failure type** supported by ChaosAgent AI.
3. Start the experiment.
4. ChaosAgent marks the selected service as **Failed**.
5. The Graph Engine calculates the affected dependent services.
6. The system calculates:

   * Failed service
   * Affected services
   * Propagation path
   * Propagation depth
   * Impact level
   * Critical dependencies
   * Potential SPOF
7. The AI module receives the calculated analysis.
8. The AI module generates:

   * Human-readable explanation
   * Risk interpretation
   * Recommendations
9. Record the experiment result.
10. Reset the simulation and return the topology to the normal state.

---

# 4. Baseline Scenarios

## Category 1: Service Failure

### Scenario: service_failure-01 — Payment Service

**Input**

```text
Target Service: Payment Service
Failure Type: Service Unavailable
```

**Expected System Behaviour**

```text
Payment Service → FAILED
```

The Graph Engine checks which services depend on Payment Service and calculates the propagation path.

**Expected Output**

```text
Failed Service: Payment Service
Affected Services: <calculated by graph>
Propagation Depth: <calculated>
Impact Level: <calculated>
Critical Dependency: <calculated>
```

---

### Scenario: service_failure-02 — Order Service

```text
Target Service: Order Service
Failure Type: Service Unavailable
```

The system calculates the services affected by the Order Service failure.

---

### Scenario: service_failure-03 — Database

```text
Target Service: Database
Failure Type: Service Unavailable
```

The system analyzes the dependency graph and determines how many connected services are affected.

---

### Scenario: service_failure-04 — API Gateway

```text
Target Service: API Gateway
Failure Type: Service Unavailable
```

The system calculates the downstream impact of the API Gateway failure.

---

# 5. Category 2: Dependency Failure

These scenarios test how dependency relationships influence failure propagation.

### Scenario: dependency_failure-01 — Payment → Order

```text
Target Service: Payment Service
Dependency: Order Service
```

The system analyzes the dependency relationship and identifies the resulting impact.

### Scenario: dependency_failure-02 — Order → Database

```text
Target Service: Order Service
Dependency: Database
```

The system calculates the propagation through the dependency graph.

### Scenario: dependency_failure-03 — API Gateway → Payment

```text
Target Service: API Gateway
Dependency: Payment Service
```

The system determines the downstream affected services.

### Scenario: dependency_failure-04 — API Gateway → Order

```text
Target Service: API Gateway
Dependency: Order Service
```

The system analyzes the resulting propagation.

---

# 6. Category 3: Critical Dependency Analysis

These experiments focus on identifying services whose failure can have a significant impact on the system.

### Scenario: critical_dependency-01 — Database

```text
Target Service: Database
Analysis Type: Critical Dependency
```

The system determines whether multiple services depend on the Database.

Expected analysis:

```text
Critical Node: Database
Potential SPOF: Yes/No
Reason: <generated from dependency analysis>
```

---

### Scenario: critical_dependency-02 — Payment Service

```text
Target Service: Payment Service
Analysis Type: Critical Dependency
```

The system evaluates the importance of Payment Service within the topology.

---

### Scenario: critical_dependency-03 — Order Service

```text
Target Service: Order Service
Analysis Type: Critical Dependency
```

The system evaluates downstream dependencies and propagation impact.

---

### Scenario: critical_dependency-04 — API Gateway

```text
Target Service: API Gateway
Analysis Type: Critical Dependency
```

The system evaluates the gateway's position within the topology.

---

# 7. Category 4: Propagation Depth Analysis

These experiments verify the Graph Engine's ability to calculate propagation depth.

### Scenario: propagation_depth-01

```text
Target: Payment Service
```

Record:

```text
Propagation Path: <calculated>
Propagation Depth: <calculated>
Affected Services: <calculated>
```

### Scenario: propagation_depth-02

```text
Target: Order Service
```

Record the calculated propagation path and depth.

### Scenario: propagation_depth-03

```text
Target: Database
```

Record the calculated affected services and propagation depth.

### Scenario: propagation_depth-04

```text
Target: API Gateway
```

Record the calculated propagation path and depth.

---

# 8. Category 5: Impact Analysis

These experiments verify that ChaosAgent correctly classifies the impact of a simulated failure.

### Scenario: impact_analysis-01 — Low Impact

Select a service with limited downstream dependencies.

Record:

```text
Failed Service: <service>
Affected Services: <calculated>
Impact Level: LOW
```

---

### Scenario: impact_analysis-02 — Medium Impact

Select a service with moderate downstream dependencies.

Record:

```text
Failed Service: <service>
Affected Services: <calculated>
Impact Level: MEDIUM
```

---

### Scenario: impact_analysis-03 — High Impact

Select a service with significant downstream dependencies.

Record:

```text
Failed Service: <service>
Affected Services: <calculated>
Impact Level: HIGH
```

---

### Scenario: impact_analysis-04 — Critical Impact

Select the most central/critical service in the topology.

Record:

```text
Failed Service: <service>
Affected Services: <calculated>
Impact Level: CRITICAL
```

---

# 9. AI Explanation Validation

For each experiment, verify that the AI explanation is based on the **Graph Engine's calculated result**.

The AI should explain:

1. Which service failed.
2. Which services were affected.
3. How the failure propagated.
4. Why the impact level was assigned.
5. Which dependency is critical.
6. Whether a potential SPOF exists.
7. What recommendations can improve resilience.

### Important Architecture Rule

```text
Graph Engine
     ↓
Deterministic Analysis
     ↓
Structured Result
     ↓
LLM
     ↓
Explanation + Recommendations
```

The LLM must **not independently invent the propagation result**.

---

# 10. Recording Results

For every experiment, record:

```text
experiment_id
experiment_category
target_service
failure_type
affected_services
propagation_path
propagation_depth
impact_level
critical_node
potential_spof
ai_explanation
recommendations
```

Example:

```text
EXP-001
service_failure
Payment Service
Service Unavailable
Order Service, Database
Payment → Order → Database
2
HIGH
Database
Yes
<AI generated explanation>
<AI generated recommendations>
```

---

# 11. Reset Procedure

After every experiment:

1. Click **Reset Simulation**.
2. Verify that the failed node returns to **Healthy**.
3. Verify that affected nodes return to their normal state.
4. Confirm that the original topology is restored.
5. Start the next experiment only after the previous simulation has been reset.

---

# 12. Expected Final Result

After completing the baseline experiments, ChaosAgent AI should be able to demonstrate:

```text
User selects service
        ↓
Failure simulation
        ↓
Graph-based propagation analysis
        ↓
Affected services identified
        ↓
Impact calculated
        ↓
Critical dependency identified
        ↓
Potential SPOF identified
        ↓
LLM explanation generated
        ↓
Recommendations generated
        ↓
Experiment recorded
        ↓
Simulation reset
```

---

# 13. Safety

ChaosAgent AI is designed for **controlled simulation and analysis**.

The baseline experiments should be performed on the application's simulated/local topology and should not intentionally disrupt production services or infrastructure.

---

# 14. Core Principle

> ChaosAgent AI calculates failure impact using graph-based deterministic analysis and uses AI to explain the result and provide recommendations.

This separation keeps the analysis explainable, reproducible, and easier to validate.
