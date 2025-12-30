# Pre-Coding Checklist (Spec-Driven, AI-Native)

## 1) Vision & Goals
- Project Goal: {{project_goal}}
- User Persona: {{user_persona}}
- Key Outcomes: {{key_outcomes}}
- Must / Must-Not: {{must_rules}} / {{must_not_rules}}

## 2) Scope & Acceptance
- In-Scope: {{in_scope}}
- Out-of-Scope: {{out_scope}}
- Acceptance (Given–When–Then):
  - Given: {{given_context}}
  - When: {{action}}
  - Then: {{expected_outcome}}

## 3) Architecture Decisions (ADRs)
- Frontend: {{frontend_stack}} (e.g., Next.js)
- Backend: {{backend_stack}} (e.g., FastAPI)
- DB: {{database}} (e.g., Neon PostgreSQL)
- Auth: {{auth_strategy}} (e.g., Better Auth with JWT)
- Messaging: {{messaging}} (e.g., Kafka + Dapr)
- Deployment: {{deploy_target}} (e.g., Docker, Minikube, Helm, AKS/GKE)
- Stateless Rule: {{stateless_constraints}}

## 4) Data & API Specs
- Task Schema (JSON): id, title, desc, due, priority, tags, completed, recurrence
- API Endpoints: {{endpoint_list}}
- Request/Response Examples: {{api_examples}}
- Status Codes & Errors: {{error_contract}}
- Search/Filter/Sort Rules: {{query_rules}}
- Versioning: api@v1, schema@v1

## 5) Events & Workflows
- Topics: reminders, audit, recurrence, sync
- Event Payloads: {{event_payload_schemas}}
- Idempotency Keys: {{idempotency_strategy}}
- Triggers/SLAs/Retries/Timeouts: {{event_sla}}

## 6) Security & Compliance
- AuthN/AuthZ Flow: {{authn_authz_flow}}
- Roles/Permissions: {{roles_matrix}}
- Secrets Strategy: {{env_secrets_strategy}}
- PII Policy & Retention: {{data_policy}}
- Threats & Mitigations: {{threat_model}}

## 7) Environments & Config
- Envs: dev / staging / prod
- Env Vars: {{env_vars}}
- Feature Flags: {{flags}}
- Observability: logs, metrics, traces → {{observability_plan}}
- Error Handling Codes/Messages: {{error_handling_spec}}

## 8) AI-Native Assets
- Skills: httpGet, retry, cache, validateJson, summarizeText
- Templates: FeatureSpec@v1, APIRequest@v1, BugReport@v1, ResearchPrompt@v1
- Sub-Agents: SpecEngineer, CodeGenOrchestrator, QAAgent, OpsAgent
- Registries: SkillRegistry / TemplateRegistry / AgentRegistry lookup rules

## 9) Testing Plan
- Unit (Given–When–Then): {{unit_cases}}
- Contract (API schema): {{contract_tests}}
- E2E User Journeys: {{e2e_flows}}
- Event Tests: reminder trigger → delivery → audit verify: {{event_tests}}

## 10) Non-Functional Requirements
- Performance Targets: {{performance_targets}}
- Reliability & Degradation: {{reliability_rules}}
- Scalability Limits: {{scale_rules}}
- Availability SLO/SLA: {{availability_targets}}

## 11) Risks & Assumptions
- Risks: {{major_risks}}
- Assumptions: {{assumptions}}
- Mitigations: {{mitigations}}

## 12) CI/CD & Release
- Build/Test/Deploy Stages: {{cicd_stages}}
- Gates/Approvals: {{cicd_gates}}
- Lint/Typecheck Commands: {{lint_type_commands}}
- Release Notes/Changelog: {{release_process}}

## 13) Submission & Demo
- Repo Structure (Monorepo): frontend / backend / specs
- Live Link Plan: {{hosting_target}} (e.g., Vercel)
- Demo Script ≤ 90s: {{demo_points}}
- Contact: {{whatsapp_number}}

## Definition of Done (Pre-Coding)
- Specs freeze: schemas, APIs, events, security, tests defined
- AI assets ready: skills, templates, sub-agents registered
- Toolchain set: CI/CD + lint/typecheck commands documented
- Acceptance checklist passes on paper (no manual coding)

---

## Ultra-Short Roman (Quick Fill)
- Pehle specs finalize + tests likho
- ADRs + data/API/events/security set karo
- AI skills/templates/sub-agents ready rakho
- CI/CD, envs, observability plan likh lo
- Manual coding nahi; sirf spec → AI codegen
