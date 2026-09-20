# ChaosAgent AI

[svg](https://github.com/harshit-sharma08/ChaosAgent-AI-Graph-Driven-Autonomous-Chaos-Engineering-Failure-Topology-Simulator/edit/main)

**AI-powered chaos engineering for dependency graph analysis, failure prediction, blast-radius simulation, controlled fault injection, and resilience improvement — in one workflow.**

> ⚠️ **Educational prototype.** Designed for controlled testing and experimentation in non-production environments.

## 1. Project Overview

[svg](YOUR_GITHUB_README_LINK#1-project-overview)

ChaosAgent AI demonstrates how AI-assisted chaos engineering can help engineering teams understand service dependencies, identify potential failure scenarios, analyze blast radius, and safely test system resilience before failures become major incidents. The core workflow:

```text
SYSTEM TELEMETRY → DEPENDENCY GRAPH → AI ANALYSIS → FAILURE SCENARIO → BLAST-RADIUS SIMULATION → CONTROLLED CHAOS EXPERIMENT → RESILIENCE INSIGHTS
```

**svg**

ChaosAgent AI collects system and service information from sources such as Kubernetes, observability/telemetry data, and configured service information. It builds a dependency graph showing how services are connected and which components depend on each other. The AI layer analyzes this graph to identify important failure scenarios, estimates their potential impact, and helps select controlled chaos experiments. Before applying a failure to a running test environment, the system can analyze the expected blast radius and then execute the experiment within defined safety boundaries. The resulting observations are used to identify weak dependencies, understand cascading failures, and generate resilience insights for improving the system.
