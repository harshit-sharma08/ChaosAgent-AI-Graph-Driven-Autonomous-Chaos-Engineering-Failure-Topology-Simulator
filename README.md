# ChaosAgent AI



**AI-powered chaos engineering for dependency graph analysis, failure prediction, blast-radius simulation, controlled fault injection, and resilience improvement — in one workflow.**

> ⚠️ **Educational prototype.** Designed for controlled testing and experimentation in non-production environments.

## 1. Project Overview



ChaosAgent AI demonstrates how AI-assisted chaos engineering can help engineering teams understand service dependencies, identify potential failure scenarios, analyze blast radius, and safely test system resilience before failures become major incidents. The core workflow:

```text
SYSTEM TELEMETRY → DEPENDENCY GRAPH → AI ANALYSIS → FAILURE SCENARIO → BLAST-RADIUS SIMULATION → CONTROLLED CHAOS EXPERIMENT → RESILIENCE INSIGHTS
```

**svg**

ChaosAgent AI collects system and service information from sources such as Kubernetes, observability/telemetry data, and configured service information. It builds a dependency graph showing how services are connected and which components depend on each other. The AI layer analyzes this graph to identify important failure scenarios, estimates their potential impact, and helps select controlled chaos experiments. Before applying a failure to a running test environment, the system can analyze the expected blast radius and then execute the experiment within defined safety boundaries. The resulting observations are used to identify weak dependencies, understand cascading failures, and generate resilience insights for improving the system.

## 2. Features



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



ChaosAgent AI follows a graph-driven chaos engineering architecture. The system collects service and observability information from sources such as Kubernetes, OpenTelemetry traces, eBPF-based metrics, and configured system data. This information is used to build a dependency graph representing relationships between services. The AI agent analyzes the graph to identify potential failure scenarios and estimate their possible blast radius. Selected experiments are then executed in a controlled environment through the chaos experiment layer, while safety guardrails limit the experiment scope and provide mechanisms to stop or roll back unsafe experiments. Finally, the collected results are analyzed to identify failure propagation, weak dependencies, and opportunities to improve system resilience.

## 4. Tech Stack



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


### Prerequisites



* Python 3.10+
* Docker
* Kubernetes / Minikube or another Kubernetes environment
* Git
* OpenTelemetry-compatible telemetry source
* eBPF-compatible Linux environment for eBPF-based monitoring
* Required AI/LLM API credentials if an external LLM provider is configured
* Node.js only if the project repository contains a separate web dashboard/frontend

* ### 6.1 Clone & Install



```text
# Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd chaosagent-ai

# Install project dependencies
# Follow the dependency instructions provided by the individual
# services/modules in the repository.

# Configure the required environment variables
# Copy the example environment file if provided:
cp .env.example .env
```

**svg**

> **Note:** ChaosAgent AI depends on infrastructure and observability components such as Kubernetes, telemetry sources, and the configured AI/experiment environment. Make sure the required dependencies are available before running chaos experiments.

### 6.2 Environment Variables



**`.env`**

```text
# AI / LLM configuration
LLM_PROVIDER=mock
LLM_API_KEY=

# Kubernetes configuration
KUBERNETES_NAMESPACE=default

# Observability configuration
OTEL_ENDPOINT=
EBPF_ENABLED=false

# Chaos experiment configuration
EXPERIMENT_MODE=staging
EXPERIMENT_TIMEOUT=
MAX_BLAST_RADIUS=

# Safety configuration
ENABLE_GUARDRAILS=true
ENABLE_ROLLBACK=true
```

**svg**

> **Note:** The exact environment variables depend on the modules and integrations enabled in the current implementation. Do not add production credentials or unrestricted infrastructure access to local development configuration.

**Never commit real API keys or credentials.** Keep secrets only in local `.env` files or the project's configured secret-management system.

## 7. Running Locally



Start the required infrastructure and application components according to the repository configuration.

```text
# Start the required development environment
# Example:

docker compose up

# or start the required services individually
# according to the project configuration.
```

**svg**

If Kubernetes is required for the current experiment, start a local Kubernetes environment such as Minikube or another supported cluster before running the experiment.

```text
# Verify Kubernetes connectivity
kubectl get nodes

# Verify the required workloads
kubectl get pods
```

**svg**

> **Important:** Run chaos experiments only against the intended development, staging, or isolated test environment. Do not point experimental fault injection at production infrastructure without appropriate authorization and safety controls.

## 8. Demo Workflow


1. Start the required ChaosAgent AI services and supporting infrastructure.
2. Provide the system with service, telemetry, and configuration information.
3. Build or load the dependency graph representing the relationships between services.
4. Review the generated topology to understand service dependencies.
5. Let the AI analysis layer identify potential failure scenarios.
6. Select a controlled experiment for the configured test environment.
7. Analyze the expected blast radius before executing the experiment.
8. Run the selected chaos experiment within the configured safety boundaries.
9. Observe the affected services and system behavior through telemetry and monitoring data.
10. Review the resulting failure propagation and resilience insights.
11. Use the identified weak points to improve mechanisms such as circuit breakers, rate limiting, fallback handling, or service dependencies.

9. API Documentation



Core System Interfaces



The exact API routes depend on the backend implementation present in the repository. The main logical operations exposed by ChaosAgent AI are:

Operation	Description
Dependency Graph	Build or update the service dependency graph
Telemetry Ingestion	Collect service and observability information
Graph Analysis	Analyze relationships between services
Failure Planning	Identify potential failure scenarios
Blast-Radius Analysis	Estimate affected downstream services
Experiment Configuration	Configure a controlled chaos experiment
Experiment Execution	Execute the selected failure scenario
Experiment Status	Monitor the running experiment
Experiment Stop / Rollback	Stop or roll back an unsafe experiment
Resilience Analysis	Analyze system behavior after the experiment
Insights	Return failure impact and resilience recommendations



Note: Add the exact GET/POST/PUT/DELETE routes from the current backend implementation here once the repository API is finalized. This avoids documenting endpoints that are not actually present in the project.

10. System / Data Model



The core data handled by ChaosAgent AI can be represented through the following logical components:

Service
   |
   ├── Service Dependency
   |
   ├── Telemetry / Metric
   |
   ├── Failure Scenario
   |
   ├── Experiment
   |
   ├── Blast-Radius Result
   |
   └── Resilience Insight

svg

The dependency graph represents services as nodes and their relationships as edges. Telemetry provides additional information about service behavior, while experiment records describe the failure scenario, scope, execution state, and observed impact. Blast-radius analysis connects the failure scenario to the services that may be affected.

Note: The exact storage technology and schema should be updated here according to the database or graph-storage implementation currently present in the repository.

11. Project Limitations

svg

The project is an educational prototype and should not be treated as a production-ready autonomous chaos engineering platform.
The quality of dependency analysis depends on the telemetry, Kubernetes information, and service configuration available to the system.
Blast-radius analysis is dependent on the accuracy and completeness of the generated dependency graph.
AI-generated experiment recommendations should be reviewed before execution.
Chaos experiments should be restricted to controlled development, staging, or isolated environments.
Advanced autonomous experiment selection and predictive capabilities may require additional implementation and validation.
eBPF-based monitoring depends on a compatible Linux environment and the required kernel capabilities.
External LLM providers may require API credentials and can introduce external service dependencies.
The system should not be given unrestricted production access merely to perform an experiment.
12. Future Improvements

svg

More accurate predictive blast-radius analysis using historical telemetry and failure data.
Advanced graph-based failure propagation and dependency analysis.
Reinforcement-learning-based experiment selection.
Multi-cluster and multi-cloud dependency graph support.
Deeper OpenTelemetry and eBPF integrations.
More chaos experiment types and configurable experiment templates.
Advanced guardrails with automatic experiment termination and rollback.
CI/CD integration for automated resilience testing.
Resilience scorecards and historical MTTR tracking.
Automated remediation recommendations based on observed failure patterns.
Gradual expansion toward autonomous chaos experiment planning and resilience validation.

Built as an educational Chaos Engineering and AI project.
