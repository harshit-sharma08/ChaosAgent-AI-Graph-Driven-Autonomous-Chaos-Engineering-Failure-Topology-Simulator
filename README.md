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

* ## 3. Architecture

[svg](YOUR_GITHUB_README_LINK#3-architecture)

```text
Kubernetes / OpenTelemetry / eBPF / Config
                 |
                 v
        Telemetry & Data Layer
                 |
                 v
       Dependency Graph Engine
                 |
                 v
          AI Agent Layer
        ├── Graph Analysis
        ├── Failure Scenario Planning
        ├── Blast-Radius Analysis
        └── Experiment Selection
                 |
                 v
       Chaos Experiment Engine
        ├── Latency Injection
        ├── Pod / Service Failure
        └── DB Connection Pool Exhaustion
                 |
                 v
       Safety & Guardrail Layer
        ├── Experiment Limits
        ├── Scope Control
        └── Rollback / Stop
                 |
                 v
        Resilience Insights
        ├── Failure Impact
        ├── Affected Services
        └── Resilience Recommendations
```

**svg**

ChaosAgent AI follows a graph-driven chaos engineering architecture. The system collects service and observability information from sources such as Kubernetes, OpenTelemetry traces, eBPF-based metrics, and configured system data. This information is used to build a dependency graph representing relationships between services. The AI agent analyzes the graph to identify potential failure scenarios and estimate their possible blast radius. Selected experiments are then executed in a controlled environment through the chaos experiment layer, while safety guardrails limit the experiment scope and provide mechanisms to stop or roll back unsafe experiments. Finally, the collected results are analyzed to identify failure propagation, weak dependencies, and opportunities to improve system resilience.

## 4. Tech Stack

[svg](YOUR_GITHUB_README_LINK#4-tech-stack)

| **Layer**         | **Technologies**                                                      |
| ----------------- | --------------------------------------------------------------------- |
| Infrastructure    | Kubernetes, Containers                                                |
| Observability     | OpenTelemetry, eBPF                                                   |
| Graph / Topology  | Dependency Graph, Graph-based Analysis                                |
| AI / Intelligence | LLM-based AI Agent, Graph Analysis                                    |
| Chaos Engineering | Fault Injection, Controlled Experiments                               |
| Experiment Types  | Latency Injection, Pod/Service Failure, DB Connection Pool Exhaustion |
| Configuration     | YAML / Configuration Files                                            |
| Insights          | Failure Analysis, Blast-Radius Analysis, Resilience Metrics           |

## 5. Project Structure

[svg](YOUR_GITHUB_README_LINK#5-project-structure)

```text
chaosagent-ai/
├── config/                 Configuration files
├── graph/                  Dependency graph and topology logic
├── agent/                  AI agent and experiment planning
├── experiments/            Chaos experiment definitions
├── telemetry/              Observability and telemetry integration
├── guardrails/             Experiment safety and control logic
├── analysis/               Failure and blast-radius analysis
├── insights/               Resilience insights and recommendations
└── README.md               Project documentation
```

**svg**

> **Note:** The exact folder structure may vary depending on the current implementation in the repository. The structure above represents the logical architecture of the ChaosAgent AI project.

## 6. Installation

[svg](YOUR_GITHUB_README_LINK#6-installation)

### Prerequisites

[svg](YOUR_GITHUB_README_LINK#prerequisites)

* Python 3.10+
* Docker
* Kubernetes / Minikube or another Kubernetes environment
* Git
* OpenTelemetry-compatible telemetry source
* eBPF-compatible Linux environment for eBPF-based monitoring
* Required AI/LLM API credentials if an external LLM provider is configured
* Node.js only if the project repository contains a separate web dashboard/frontend

