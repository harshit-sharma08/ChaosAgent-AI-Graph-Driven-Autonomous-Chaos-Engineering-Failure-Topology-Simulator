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

## 2. Features

[svg](YOUR_GITHUB_README_LINK#2-features)

* **Dependency graph generation** — service and system information is used to build a dependency graph that represents how different services communicate and depend on each other.

* **Telemetry & observability integration** — collects available service and system signals from sources such as OpenTelemetry traces, eBPF-based metrics, Kubernetes information, and configured observability data.

* **AI-assisted failure planning** — analyzes the dependency graph to identify important failure scenarios and helps determine which components should be tested for resilience.

* **Failure scenario simulation** — evaluates a proposed failure scenario before executing the experiment to understand which services and dependencies may be affected.

* **Blast-radius analysis** — identifies the potential downstream impact of a service failure and shows how a local failure can propagate through connected services.

* **Controlled chaos experiments** — supports controlled failure scenarios such as latency injection, service/pod termination, and database connection-pool exhaustion in a test or staging environment.

* **Safety guardrails** — experiments are designed to operate within predefined boundaries so that unsafe or excessive failures can be stopped or rolled back.

* **Resilience validation** — observes system behavior during experiments to evaluate mechanisms such as circuit breakers, rate limiters, fallback mechanisms, and other resilience controls.

* **Failure topology visualization** — represents service relationships and potential failure propagation through a graph-based view, making complex dependencies easier to understand.

* **Resilience insights** — converts experiment observations and dependency analysis into actionable information about weak points, affected services, and areas where system resilience can be improved.

* **Experiment configuration** — supports configuration-driven chaos scenarios so that failure parameters and experiment boundaries can be defined before execution.

* **Staging / canary experimentation** — designed to perform controlled experiments in isolated or limited environments before considering broader system testing.
