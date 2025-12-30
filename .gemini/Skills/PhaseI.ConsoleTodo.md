# Phase I — Console Todo App (Spec-Driven, AI-Native)

## Objective
- Python-based, in-memory Todo CLI
- Manual coding disallowed; code must be generated via Gemini CLI using this spec
- Deliver basic features: add, delete, update, list/view, complete

## Scope
- In-Scope: core CRUD + complete toggle; CLI UX; validation; help/usage
- Out-of-Scope: persistence (disk/DB), auth, tags/priority, reminders/recurrence, web UI

## CLI Commands & Syntax
- `todo add "Title" [--desc "Description"]`
  - Creates a new task; prints task summary
- `todo list [--completed | --pending] [--sort created|title] [--format json|table]`
  - Lists tasks; default `--pending`; default `--format table`
- `todo view <id> [--format json|table]`
  - Shows one task by id
- `todo update <id> [--title "New Title"] [--desc "New Desc"]`
  - Updates fields; prints updated summary
- `todo complete <id>`
  - Marks a task as completed; idempotent
- `todo delete <id>`
  - Deletes a task by id; prints confirmation
- `todo help`
  - Shows usage and examples

## Data Model (JSON Schema)
```json
{
  "$id": "task.schema@v1",
  "type": "object",
  "required": ["id", "title", "completed", "created_at", "updated_at"],
  "properties": {
    "id": { "type": "integer", "minimum": 1 },
    "title": { "type": "string", "minLength": 1, "maxLength": 120 },
    "desc": { "type": "string", "maxLength": 1000 },
    "completed": { "type": "boolean" },
    "created_at": { "type": "string", "format": "date-time" },
    "updated_at": { "type": "string", "format": "date-time" }
  },
  "additionalProperties": false
}
```
- ID policy: auto-increment integer starting at 1
- Timestamps: ISO-8601; `updated_at` changes on any mutation

## State & Behavior
- Storage: in-memory list of tasks (process-local)
- Idempotency:
  - `complete <id>` on already-completed returns success without change
  - `delete <id>` on missing id returns error
- Sorting: `created` ascending; `title` lexicographic

## Validation & Errors
- Title required for `add`; `minLength=1`, `maxLength=120`
- `id` must exist for `view/update/complete/delete`
- Exit codes: `0` success, `1` validation error, `2` not found, `3` usage error
- Error messages: concise, actionable; when `--format json` emit structured error `{code, message, details}`

## Output Formats
- `table`: headers `ID | Title | Completed | Created | Updated`
- `json`: arrays or objects strictly conforming to schema; no extra fields

## Help/Usage Content
- Show command list, flags, examples:
  - `todo add "Buy milk" --desc "2 liters"`
  - `todo list --pending --sort title`
  - `todo update 3 --title "Buy oat milk"`
  - `todo complete 3`
  - `todo delete 3`

## Acceptance Criteria (Given–When–Then)
- Add:
  - Given empty state; When `todo add "Task A"`; Then list shows `Task A` with `completed=false`
- List:
  - Given 2 tasks pending; When `todo list`; Then prints both in table (default pending)
- Complete:
  - Given `Task A` id=1; When `todo complete 1`; Then `completed=true` and `updated_at` changes
- Update:
  - Given `Task A` id=1; When `todo update 1 --title "Task A+"`; Then title updated and echoed
- View:
  - Given `Task A` id=1; When `todo view 1 --format json`; Then JSON matches schema
- Delete:
  - Given `Task A` id=1; When `todo delete 1`; Then list no longer shows id=1
- Errors:
  - Given no task 999; When `todo view 999`; Then exit code=2 and error message
  - Given empty title; When `todo add ""`; Then exit code=1 and validation error

## Non-Functional Requirements
- Startup: instant; commands return within < 200ms for <100 tasks
- Cross-platform: Windows/macOS/Linux; Python 3.10+
- Deterministic outputs: same inputs → same printed outputs

## Observability
- Logging: minimal; only errors to stderr; `--format json` includes `{code,message,details}`
- Telemetry: none (Phase I)

## Codegen Contract (Gemini CLI)
- Tooling: Gemini CLI with `GEMINI_API_KEY` env
- Prompt Template (GeminiPrompt@v1):
  - System: “Implement Python CLI matching the provided Spec. No extra features.”
  - Constraints: “Python 3.10+, no external deps except stdlib, structured outputs.”
  - Files:
    - `todo/__main__.py` entrypoint (argparse)
    - `todo/state.py` in-memory store
    - `todo/models.py` dataclass `Task`
    - `todo/cli.py` command handlers
    - `README.md` usage (auto-generated)
- Tests:
  - `tests/test_cli.py` with scenarios from Acceptance Criteria
- Commands:
  - Generate: `gemini codegen -p specs/PhaseI.ConsoleTodo.claude.md -o ./`
  - Verify: run tests, ensure exit codes and outputs match

## Definition of Done (Phase I)
- All acceptance scenarios pass (manual run + tests)
- CLI help shows commands and examples
- JSON outputs validate against schema
- No manual coding performed; changes traceable to codegen prompts/spec
