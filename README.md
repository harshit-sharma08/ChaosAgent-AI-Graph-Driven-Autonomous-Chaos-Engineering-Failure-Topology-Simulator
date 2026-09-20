ChaosAgent AI
Graph-driven autonomous chaos engineering: dependency analysis, failure planning, blast-radius prediction, controlled chaos experiments, and resilience insights in one workflow.
IMPORTANT: This is an educational / development prototype. ChaosAgent AI is designed to demonstrate AI-assisted chaos engineering and resilience testing for distributed systems. Experiments should be performed only in controlled development, staging, or explicitly authorized environments. Never run fault-injection experiments against systems without proper authorization and safety controls.
---
Table of Contents
Project Overview
Features
Architecture
Tech Stack
Project Structure
Installation
Running Locally
Demo Workflow
API Documentation
Dependency Graph Model
Blast-Radius Analysis
Safety and Guardrails
Database / Graph Data Model
Example Experiment
Project Limitations
Future Improvements
Roadmap
Vision
Team
Disclaimer
---
1. Project Overview
ChaosAgent AI is an AI-assisted chaos engineering platform. It understands how services in a distributed software system depend on each other, identifies potentially high-impact failure scenarios, estimates their blast radius, and safely plans controlled chaos experiments.
Modern microservice-based applications can contain hundreds or thousands of interconnected services. A failure in one service can propagate through its dependencies and cause a much larger system outage.
ChaosAgent AI aims to move chaos engineering from a mostly manual and reactive process toward a graph-aware, intelligent, and proactive workflow.
Core Workflow
```text
SYSTEM DATA → DEPENDENCY GRAPH → AI ANALYSIS → FAILURE PLANNING
      → BLAST-RADIUS SIMULATION → CONTROLLED INJECTION
      → RESULT ANALYSIS → RESILIENCE RECOMMENDATIONS
```
How it works in short:
The system collects topology and service information from infrastructure and monitoring sources such as Kubernetes, service mesh, cloud APIs, and APM / Prometheus-style telemetry. This information is represented as a live dependency graph.
The AI agent analyzes the graph to identify important dependencies and propose high-value failure scenarios.
Before a real fault is injected, the expected impact is simulated on the dependency graph.
When an experiment is considered safe, the controlled injection layer executes a scoped failure experiment with guardrails and rollback mechanisms.
The resulting data is converted into resilience reports, impact analysis, and remediation recommendations.
---
2. Features
Live dependency graph: Continuously represents services, infrastructure components, queues, databases, and their relationships.
Graph-based topology analysis: Understands how services depend on each other and identifies important dependency paths.
AI-assisted experiment planning: Uses an AI agent to analyze the dependency graph and propose targeted failure scenarios.
Failure scenario analysis: Evaluates what could happen when an important service becomes unavailable, slow, or unhealthy.
Predictive blast-radius analysis: Estimates which downstream components may be affected before a real fault is injected.
Controlled chaos experiments: Supports scoped fault-injection experiments instead of uncontrolled system failures.
Guardrails and rollback: Safety thresholds can stop an experiment when predefined conditions are exceeded.
Resilience insights: Converts experiment results into understandable reports about system weaknesses and recovery behavior.
Remediation recommendations: Highlights areas where fallback, timeout, retry, redundancy, or dependency isolation may need improvement.
CI/CD integration concept: Designed to become part of development and deployment pipelines so resilience testing can become continuous.
Resilience scorecards (planned): Track resilience improvements, blast-radius reduction, and recovery metrics over time.
---
3. Architecture
```text
                    ┌──────────────────────────────┐
                    │         Data Sources         │
                    │                              │
                    │ Kubernetes · Service Mesh    │
                    │ Cloud APIs · APM / Metrics   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │        Graph Engine          │
                    │                              │
                    │ Live Dependency Graph        │
                    │ Topology & Impact Analysis   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       AI Agent Layer         │
                    │                              │
                    │ Graph Analysis               │
                    │ Experiment Planning          │
                    │ Failure Scenario Selection   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │ Simulation & Injection Layer │
                    │                              │
                    │ Blast-Radius Simulation      │
                    │ Controlled Fault Injection   │
                    │ Guardrails & Rollback        │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       Insights Layer         │
                    │                              │
                    │ Impact Analysis              │
                    │ Resilience Reports           │
                    │ Remediation Suggestions      │
                    └──────────────────────────────┘
```
The system is divided into five major layers.
Data Sources
Collects system information from:
Kubernetes
Service Mesh
Cloud APIs
APM / monitoring systems
Prometheus-style metrics
Graph Engine
Converts service and infrastructure relationships into a dependency graph.
```text
User
  ↓
API Gateway
  ↓
Order Service
  ├── Payment Service
  ├── Inventory Service
  └── Database
```
AI Agent Layer
The AI agent analyzes the dependency graph and identifies potentially important failure scenarios. Its main role is to answer:
```text
What should we test?
Why should we test it?
What could be affected?
```
Simulation and Injection Layer
Before performing a real experiment, the system simulates the expected impact of a failure on the dependency graph. After safety checks, a controlled fault-injection experiment can be performed in an authorized environment.
Insights Layer
The experiment results are analyzed to identify:
affected services
dependency weaknesses
recovery behavior
potential resilience improvements
experiment results and metrics
---
4. Tech Stack
Infrastructure: Kubernetes
Service Communication: Service Mesh / APIs
Monitoring: APM / Prometheus-style metrics
Graph Engine: Dependency Graph / Graph Database
AI Layer: LLM-based reasoning and experiment planning
Experiment Planning: AI Agent
Simulation: Dependency-graph based blast-radius analysis
Fault Injection: Kubernetes / Service Mesh chaos mechanisms
Backend: Python / FastAPI or Node.js-based services
Frontend: React / modern web dashboard
Data: Graph data + service telemetry
Visualization: Dependency topology and resilience dashboards
Future Intelligence: Reinforcement-learning based experiment optimization
Note: The exact technologies used in the current MVP should match the implementation in the repository. Advanced components such as reinforcement-learning-based planning, predictive simulation, multi-cloud support, and self-healing are part of the planned architecture / roadmap unless implemented in the current version.
---
5. Project Structure
A suggested project structure:
```text
chaosagent-ai/
├── frontend/          Web dashboard
├── backend/           API and orchestration layer
├── agent/             AI agent and experiment planning
├── graph-engine/      Dependency graph processing
├── simulation/        Blast-radius simulation
├── chaos-engine/      Fault injection and experiment control
├── telemetry/         Metrics and topology ingestion
├── insights/          Reports and resilience analysis
├── configs/           Experiment and safety configurations
└── README.md
```
The actual repository structure may differ depending on the current implementation.
---
6. Installation
Prerequisites
Python 3.10+
Node.js 18+
Docker
Docker Compose
Kubernetes cluster for infrastructure experiments
Git
Required LLM/API credentials if an external model is configured
For local Kubernetes experimentation, tools such as Minikube or Kind can be used.
6.1 Clone and Install
```bash
git clone <YOUR_REPOSITORY_URL>
cd chaosagent-ai
```
Backend (Python):
```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```
Frontend:
```bash
cd ../frontend
npm install
```
6.2 Environment Variables
Create a local .env file according to the configuration required by the implementation.
```env
# Backend
PORT=8000

# AI
LLM_PROVIDER=mock
LLM_API_KEY=
LLM_MODEL=

# Graph
GRAPH_DATABASE_URL=
GRAPH_DATABASE_USER=
GRAPH_DATABASE_PASSWORD=

# Kubernetes
KUBERNETES_CONTEXT=

# Monitoring
PROMETHEUS_URL=

# Frontend
FRONTEND_URL=http://localhost:3000
```
Never commit API keys, passwords, Kubernetes credentials, or other secrets to GitHub. Add .env to your .gitignore file.
---
7. Running Locally
Start the backend
```bash
cd backend

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

python -m uvicorn app.main:app --reload --port 8000
```
Start the frontend
Open another terminal:
```bash
cd frontend
npm run dev
```
Local URLs
Frontend: http://localhost:3000
Backend API: http://localhost:8000
API Docs (if FastAPI is used): http://localhost:8000/docs
---
8. Demo Workflow
The intended ChaosAgent AI workflow is:
Step 1: Start the system
Run the frontend, backend, graph engine, and required monitoring components.
Step 2: Connect system data
Provide authorized topology or telemetry data from Kubernetes, service mesh, or monitoring sources.
Step 3: Build the dependency graph
The system identifies service-to-service relationships and creates the dependency graph.
```text
Frontend
   ↓
API Gateway
   ↓
Order Service
   ├── Payment Service
   └── Inventory Service
```
Step 4: Analyze the topology
The AI agent analyzes the graph and identifies potentially important dependencies.
Step 5: Select an experiment
The agent proposes a failure scenario.
```text
Payment Service → Failure / Unavailability
```
Step 6: Simulate the blast radius
The system estimates the possible downstream impact before performing the real experiment.
```text
Payment Service
       ↓
Order Service
       ↓
Checkout
```
Step 7: Run a controlled experiment
If safety conditions are satisfied, the system performs a scoped failure experiment in an authorized test environment.
Step 8: Monitor the experiment
The system observes metrics such as:
error rate
latency
affected services
recovery time
service health
Step 9: Stop or rollback
If a safety threshold is crossed, the experiment can be stopped and rolled back.
Step 10: Generate insights
The system produces an experiment report:
```text
Experiment
    ↓
Affected Components
    ↓
Observed Impact
    ↓
Recovery Behavior
    ↓
Weak Dependency
    ↓
Resilience Recommendation
```
---
9. API Documentation
The exact API endpoints depend on the current implementation. A possible API structure is:
Topology
```text
POST /api/topology/ingest
GET  /api/topology
GET  /api/topology/graph
```
AI Agent
```text
POST /api/agent/analyze
POST /api/agent/plan
GET  /api/agent/experiments
```
Simulation
```text
POST /api/simulation/blast-radius
GET  /api/simulation/:id
```
Experiments
```text
POST /api/experiments
GET  /api/experiments
GET  /api/experiments/:id
POST /api/experiments/:id/stop
POST /api/experiments/:id/rollback
```
Insights
```text
GET /api/insights
GET /api/insights/:id
GET /api/resilience-score
```
Note: These endpoints are an architectural representation. Replace them with the actual endpoints implemented in the repository.
---
10. Dependency Graph Model
The dependency graph represents the relationships between services and infrastructure components. Each node represents a component and each edge represents a dependency or communication relationship.
```text
                ┌──────────────┐
                │   Payment    │
                │   Service    │
                └──────▲───────┘
                       │
┌─────────┐     ┌──────┴───────┐     ┌──────────────┐
│  User   │ ──> │ Order        │ ──> │  Inventory   │
└────┬────┘     │ Service      │     │  Service     │
     │          └──────┬───────┘     └──────────────┘
     │                 │
     │                 ▼
     │          ┌──────────────┐
     └────────> │   Database   │
                └──────────────┘
```
This graph allows ChaosAgent AI to reason about possible failure propagation.
---
11. Blast-Radius Analysis
Blast radius represents the possible scope of impact caused by a component failure.
```text
Payment Service
       X
       ↓
Order Service
       ↓
Checkout
```
If Payment Service becomes unavailable and Order Service depends on it, the impact may propagate downstream. ChaosAgent AI aims to estimate this impact before performing a real fault-injection experiment.
The basic process:
```text
Select Component
       ↓
Simulate Failure
       ↓
Traverse Dependency Graph
       ↓
Identify Affected Components
       ↓
Calculate / Estimate Impact
       ↓
Generate Risk Insight
```
---
12. Safety and Guardrails
Chaos engineering must be performed carefully. ChaosAgent AI is designed around controlled and authorized experiments.
Potential safety mechanisms:
experiment scope limits
service allowlists
failure-duration limits
error-rate thresholds
latency thresholds
maximum affected-service limits
automatic experiment termination
automatic rollback
staging / canary environments
manual approval for high-risk experiments
Safety loop:
```text
Experiment Started
       ↓
Monitor Metrics
       ↓
Threshold Safe?
   /          \
 Yes           No
 ↓              ↓
Continue      STOP
                ↓
             Rollback
```
The system should never be used to intentionally disrupt unauthorized infrastructure.
---
13. Database / Graph Data Model
The exact schema depends on the selected graph/database implementation. A conceptual model:
```text
Service
├── id
├── name
├── type
├── status
└── metadata

Dependency
├── source_service
├── target_service
├── protocol
└── relationship

Experiment
├── id
├── target
├── failure_type
├── duration
├── status
└── result

ExperimentResult
├── affected_services
├── error_rate
├── latency
├── recovery_time
└── observations
```
---
14. Example Experiment
Consider the following architecture:
```text
User
 ↓
API Gateway
 ↓
Order Service
 ↓
Payment Service
 ↓
Database
```
The AI agent identifies Payment Service as an important dependency and proposes:
```text
Experiment: Payment Service Unavailability
```
Before injecting the failure:
```text
Simulation
    ↓
Payment fails
    ↓
Order Service affected
    ↓
Checkout affected
```
The experiment is then executed in a controlled environment. The system observes:
```text
Error Rate
Latency
Affected Services
Recovery Time
```
The final insight could identify:
```text
Potential Weakness:
Order Service depends strongly on Payment Service.

Possible Improvement:
Improve timeout, fallback, retry, redundancy,
or dependency-isolation mechanisms.
```
---
15. Project Limitations
The project is an educational/development prototype and should not be treated as a production-ready autonomous chaos platform without additional validation.
Real production fault injection requires strong authorization, safety controls, observability, and operational review.
Predictive blast-radius analysis is an estimate and cannot guarantee the exact behavior of a real distributed system.
AI-generated experiment recommendations may require human approval, especially for high-risk environments.
The quality of the dependency graph depends on the quality and completeness of the topology/telemetry data.
Advanced reinforcement-learning-based experiment optimization may remain a future component depending on the current MVP implementation.
Multi-cloud support is part of the planned roadmap unless implemented in the current version.
Automated self-healing is a future vision and should not be considered an implemented feature unless present in the repository.
LLM-based reasoning can produce incorrect recommendations and therefore should operate with validation and guardrails.
---
16. Future Improvements
More accurate real-time dependency discovery
Advanced graph-based risk scoring
Improved predictive blast-radius simulation
Reinforcement-learning-based experiment selection
Multi-cloud support
Deeper Kubernetes and service-mesh integration
CI/CD pipeline integration
Advanced resilience scorecards
Automatic remediation recommendations
Continuous adaptive chaos experiments
Human approval workflows for high-risk experiments
Self-healing mechanisms for automatically applying validated resilience improvements
---
17. Roadmap
Phase 1: MVP
```text
Kubernetes Data
      ↓
Dependency Graph
      ↓
Basic AI Agent
      ↓
Fault Scenario Planning
```
Phase 2: Scale
```text
Multi-Cloud
     +
Service Mesh
     +
Predictive Blast Radius
     +
Resilience Dashboard
```
Phase 3: Autonomy
```text
Continuous Topology Analysis
          ↓
Adaptive Experiment Planning
          ↓
Controlled Chaos
          ↓
Automated Insights
          ↓
Remediation
          ↓
Self-Healing Loops
```
---
18. Vision
ChaosAgent AI aims to move distributed-system resilience from a reactive process to a proactive and intelligent one.
Instead of waiting for production outages to reveal hidden dependencies, organizations should be able to continuously understand their system, identify risky dependencies, safely test failure scenarios, and improve resilience before customers experience an outage.
The long-term vision:
```text
OBSERVE → UNDERSTAND → PREDICT → TEST → LEARN → IMPROVE → REPEAT
```
A world where distributed systems continuously find and improve their own weaknesses before an outage reaches the customer.
---
19. Team
Team Leader: Harshit Sharma
Team Member: Himanshu Yadav
Mentor: Prof. Yunis Ahmad
---
20. Disclaimer
IMPORTANT: ChaosAgent AI is an educational/development project. Always run experiments only on systems you own or are explicitly authorized to test. Never perform fault injection against production or third-party infrastructure without appropriate authorization, monitoring, safety controls, and rollback procedures.
---
Built as an academic project exploring AI-assisted autonomous chaos engineering and distributed-system resilience.
