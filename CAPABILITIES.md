# Grok Video capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/grok) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

Grok video generation and non-streaming chat are supported. Chat tools are returned as data; the plugin never executes model-proposed tools.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `grok_chat_completions` | `grok_chat_completions` |  |
| `grok_list_models` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `grok_list_actions` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `grok_get_prompt_guide` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `grok_get_task` | `grok_task_retrieve` | Set action=retrieve |
| `grok_get_tasks_batch` | `grok_tasks_retrieve_batch` | Set action=retrieve_batch |
| `grok_text_to_video` | `grok_generate_video` |  |
| `grok_image_to_video` | `grok_generate_video` |  |

## Parameter equivalents

- `grok_chat_completions`: `stream` → Dify submit/poll output: async=true, stream=false.
- `grok_get_tasks_batch`: `task_ids` → ids.

## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
