"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = "/grok/tasks"

ENDPOINTS = {
    "grok_generate_video": {
        "method": "POST",
        "path": "/grok/videos",
        "operation": "generate",
        "schema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"},
                "model": {
                    "enum": [
                        "grok-imagine-video-1.5-fast:reverse",
                        "grok-imagine-video:reverse",
                        "grok-imagine-video:official",
                        "grok-imagine-video-1.5:official",
                        "grok-imagine-video",
                    ],
                    "type": "string",
                },
                "image_url": {"type": "string"},
                "reference_image_urls": {"type": "array", "items": {"type": "string"}},
                "aspect_ratio": {
                    "enum": ["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3"],
                    "type": "string",
                },
                "resolution": {"enum": ["480p", "720p", "1080p"], "type": "string"},
                "duration": {"type": "integer", "minimum": 1, "maximum": 30},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "prompt": {"type": "string"},
            "model": {
                "enum": [
                    "grok-imagine-video-1.5-fast:reverse",
                    "grok-imagine-video:reverse",
                    "grok-imagine-video:official",
                    "grok-imagine-video-1.5:official",
                    "grok-imagine-video",
                ],
                "type": "string",
            },
            "image_url": {"type": "string"},
            "reference_image_urls": {"type": "array", "items": {"type": "string"}},
            "aspect_ratio": {
                "enum": ["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3"],
                "type": "string",
            },
            "resolution": {"enum": ["480p", "720p", "1080p"], "type": "string"},
            "duration": {"type": "integer", "minimum": 1, "maximum": 30},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {
            "model": "grok-imagine-video-1.5-fast:reverse",
            "resolution": "480p",
            "duration": 6,
        },
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "grok_chat_completions": {
        "method": "POST",
        "path": "/grok/chat/completions",
        "operation": "request",
        "schema": {
            "type": "object",
            "required": ["model", "messages"],
            "properties": {
                "n": {"type": ["number", "null"], "maximum": 128, "minimum": 1},
                "model": {"enum": ["grok-4.7", "grok-4.5", "grok-4", "grok-3"], "type": "string"},
                "stream": {"type": ["boolean", "null"]},
                "messages": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["role"],
                        "properties": {
                            "role": {
                                "enum": ["user", "assistant", "system", "developer", "tool"],
                                "type": "string",
                            },
                            "content": {
                                "oneOf": [
                                    {"type": "string"},
                                    {
                                        "type": "array",
                                        "items": {
                                            "oneOf": [
                                                {
                                                    "type": "object",
                                                    "required": ["type", "text"],
                                                    "properties": {
                                                        "type": {
                                                            "type": "string",
                                                            "enum": ["text"],
                                                        },
                                                        "text": {"type": "string"},
                                                    },
                                                },
                                                {
                                                    "type": "object",
                                                    "required": ["type", "image_url"],
                                                    "properties": {
                                                        "type": {
                                                            "type": "string",
                                                            "enum": ["image_url"],
                                                        },
                                                        "image_url": {
                                                            "type": "object",
                                                            "required": ["url"],
                                                            "properties": {
                                                                "url": {"type": "string"},
                                                                "detail": {
                                                                    "type": "string",
                                                                    "enum": ["auto", "low", "high"],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            ]
                                        },
                                        "minItems": 1,
                                    },
                                ]
                            },
                            "name": {"type": "string"},
                            "tool_calls": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["id", "type", "function"],
                                    "properties": {
                                        "id": {"type": "string"},
                                        "type": {"type": "string", "enum": ["function"]},
                                        "function": {
                                            "type": "object",
                                            "required": ["name", "arguments"],
                                            "properties": {
                                                "name": {"type": "string"},
                                                "arguments": {"type": "string"},
                                            },
                                        },
                                    },
                                },
                            },
                            "refusal": {"type": ["string", "null"]},
                            "tool_call_id": {"type": "string"},
                        },
                    },
                    "minItems": 1,
                },
                "max_tokens": {"type": ["number", "null"]},
                "temperature": {"type": ["number", "null"], "maximum": 2, "minimum": 0},
                "top_p": {"type": ["number", "null"], "maximum": 1, "minimum": 0},
                "frequency_penalty": {"type": ["number", "null"], "maximum": 2, "minimum": -2},
                "presence_penalty": {"type": ["number", "null"], "maximum": 2, "minimum": -2},
                "seed": {"type": ["integer", "null"]},
                "stop": {
                    "oneOf": [
                        {"type": "string"},
                        {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                            "maxItems": 4,
                        },
                    ]
                },
                "max_completion_tokens": {"type": ["integer", "null"]},
                "logprobs": {"type": ["boolean", "null"]},
                "top_logprobs": {"type": ["integer", "null"], "minimum": 0, "maximum": 20},
                "stream_options": {
                    "type": ["object", "null"],
                    "properties": {"include_usage": {"type": "boolean"}},
                },
                "parallel_tool_calls": {"type": "boolean"},
                "user": {"type": "string"},
                "reasoning_effort": {
                    "type": ["string", "null"],
                    "enum": ["minimal", "low", "medium", "high"],
                },
                "service_tier": {
                    "type": ["string", "null"],
                    "enum": ["auto", "default", "flex", "scale", "priority"],
                },
                "store": {"type": ["boolean", "null"]},
                "metadata": {
                    "type": ["object", "null"],
                    "additionalProperties": {"type": "string"},
                },
                "logit_bias": {
                    "type": ["object", "null"],
                    "additionalProperties": {"type": "integer"},
                },
                "modalities": {
                    "type": ["array", "null"],
                    "items": {"type": "string", "enum": ["text", "audio"]},
                },
                "audio": {
                    "type": ["object", "null"],
                    "required": ["voice", "format"],
                    "properties": {
                        "voice": {
                            "type": "string",
                            "enum": [
                                "alloy",
                                "ash",
                                "ballad",
                                "coral",
                                "echo",
                                "fable",
                                "nova",
                                "onyx",
                                "sage",
                                "shimmer",
                            ],
                        },
                        "format": {
                            "type": "string",
                            "enum": ["wav", "aac", "mp3", "flac", "opus", "pcm16"],
                        },
                    },
                },
                "prediction": {
                    "type": ["object", "null"],
                    "required": ["type", "content"],
                    "properties": {
                        "type": {"type": "string", "enum": ["content"]},
                        "content": {
                            "oneOf": [
                                {"type": "string"},
                                {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "required": ["type", "text"],
                                        "properties": {
                                            "type": {"type": "string", "enum": ["text"]},
                                            "text": {"type": "string"},
                                        },
                                    },
                                },
                            ]
                        },
                    },
                },
                "web_search_options": {
                    "type": "object",
                    "properties": {
                        "search_context_size": {
                            "type": "string",
                            "enum": ["low", "medium", "high"],
                        },
                        "user_location": {
                            "type": ["object", "null"],
                            "properties": {
                                "type": {"type": "string", "enum": ["approximate"]},
                                "approximate": {
                                    "type": "object",
                                    "properties": {
                                        "country": {"type": "string"},
                                        "region": {"type": "string"},
                                        "city": {"type": "string"},
                                        "timezone": {"type": "string"},
                                    },
                                },
                            },
                        },
                    },
                },
                "tools": {
                    "type": ["array", "null"],
                    "items": {
                        "type": "object",
                        "required": ["type", "function"],
                        "properties": {
                            "type": {"type": "string", "enum": ["function"]},
                            "function": {
                                "type": "object",
                                "required": ["name"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                    "parameters": {"type": "object", "additionalProperties": True},
                                },
                            },
                        },
                    },
                },
                "tool_choice": {
                    "oneOf": [
                        {"type": "string", "enum": ["none", "auto", "required"]},
                        {
                            "type": "object",
                            "required": ["type", "function"],
                            "properties": {
                                "type": {"type": "string", "enum": ["function"]},
                                "function": {
                                    "type": "object",
                                    "required": ["name"],
                                    "properties": {"name": {"type": "string"}},
                                },
                            },
                        },
                    ]
                },
                "response_format": {
                    "oneOf": [
                        {
                            "type": "object",
                            "required": ["type"],
                            "properties": {"type": {"enum": ["text"], "type": "string"}},
                        },
                        {
                            "type": "object",
                            "required": ["type"],
                            "properties": {"type": {"enum": ["json_object"], "type": "string"}},
                        },
                        {
                            "type": "object",
                            "required": ["type", "json_schema"],
                            "properties": {
                                "type": {"enum": ["json_schema"], "type": "string"},
                                "json_schema": {
                                    "type": "object",
                                    "required": ["name"],
                                    "properties": {
                                        "name": {"type": "string"},
                                        "description": {"type": "string"},
                                        "schema": {"type": "object", "additionalProperties": True},
                                        "strict": {"type": ["boolean", "null"]},
                                    },
                                },
                            },
                        },
                    ]
                },
            },
        },
        "properties": {
            "n": {"type": ["number", "null"], "maximum": 128, "minimum": 1},
            "model": {"enum": ["grok-4.7", "grok-4.5", "grok-4", "grok-3"], "type": "string"},
            "stream": {"type": ["boolean", "null"]},
            "messages": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["role"],
                    "properties": {
                        "role": {
                            "enum": ["user", "assistant", "system", "developer", "tool"],
                            "type": "string",
                        },
                        "content": {
                            "oneOf": [
                                {"type": "string"},
                                {
                                    "type": "array",
                                    "items": {
                                        "oneOf": [
                                            {
                                                "type": "object",
                                                "required": ["type", "text"],
                                                "properties": {
                                                    "type": {"type": "string", "enum": ["text"]},
                                                    "text": {"type": "string"},
                                                },
                                            },
                                            {
                                                "type": "object",
                                                "required": ["type", "image_url"],
                                                "properties": {
                                                    "type": {
                                                        "type": "string",
                                                        "enum": ["image_url"],
                                                    },
                                                    "image_url": {
                                                        "type": "object",
                                                        "required": ["url"],
                                                        "properties": {
                                                            "url": {"type": "string"},
                                                            "detail": {
                                                                "type": "string",
                                                                "enum": ["auto", "low", "high"],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        ]
                                    },
                                    "minItems": 1,
                                },
                            ]
                        },
                        "name": {"type": "string"},
                        "tool_calls": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["id", "type", "function"],
                                "properties": {
                                    "id": {"type": "string"},
                                    "type": {"type": "string", "enum": ["function"]},
                                    "function": {
                                        "type": "object",
                                        "required": ["name", "arguments"],
                                        "properties": {
                                            "name": {"type": "string"},
                                            "arguments": {"type": "string"},
                                        },
                                    },
                                },
                            },
                        },
                        "refusal": {"type": ["string", "null"]},
                        "tool_call_id": {"type": "string"},
                    },
                },
                "minItems": 1,
            },
            "max_tokens": {"type": ["number", "null"]},
            "temperature": {"type": ["number", "null"], "maximum": 2, "minimum": 0},
            "top_p": {"type": ["number", "null"], "maximum": 1, "minimum": 0},
            "frequency_penalty": {"type": ["number", "null"], "maximum": 2, "minimum": -2},
            "presence_penalty": {"type": ["number", "null"], "maximum": 2, "minimum": -2},
            "seed": {"type": ["integer", "null"]},
            "stop": {
                "oneOf": [
                    {"type": "string"},
                    {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 4},
                ]
            },
            "max_completion_tokens": {"type": ["integer", "null"]},
            "logprobs": {"type": ["boolean", "null"]},
            "top_logprobs": {"type": ["integer", "null"], "minimum": 0, "maximum": 20},
            "stream_options": {
                "type": ["object", "null"],
                "properties": {"include_usage": {"type": "boolean"}},
            },
            "parallel_tool_calls": {"type": "boolean"},
            "user": {"type": "string"},
            "reasoning_effort": {
                "type": ["string", "null"],
                "enum": ["minimal", "low", "medium", "high"],
            },
            "service_tier": {
                "type": ["string", "null"],
                "enum": ["auto", "default", "flex", "scale", "priority"],
            },
            "store": {"type": ["boolean", "null"]},
            "metadata": {"type": ["object", "null"], "additionalProperties": {"type": "string"}},
            "logit_bias": {"type": ["object", "null"], "additionalProperties": {"type": "integer"}},
            "modalities": {
                "type": ["array", "null"],
                "items": {"type": "string", "enum": ["text", "audio"]},
            },
            "audio": {
                "type": ["object", "null"],
                "required": ["voice", "format"],
                "properties": {
                    "voice": {
                        "type": "string",
                        "enum": [
                            "alloy",
                            "ash",
                            "ballad",
                            "coral",
                            "echo",
                            "fable",
                            "nova",
                            "onyx",
                            "sage",
                            "shimmer",
                        ],
                    },
                    "format": {
                        "type": "string",
                        "enum": ["wav", "aac", "mp3", "flac", "opus", "pcm16"],
                    },
                },
            },
            "prediction": {
                "type": ["object", "null"],
                "required": ["type", "content"],
                "properties": {
                    "type": {"type": "string", "enum": ["content"]},
                    "content": {
                        "oneOf": [
                            {"type": "string"},
                            {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "required": ["type", "text"],
                                    "properties": {
                                        "type": {"type": "string", "enum": ["text"]},
                                        "text": {"type": "string"},
                                    },
                                },
                            },
                        ]
                    },
                },
            },
            "web_search_options": {
                "type": "object",
                "properties": {
                    "search_context_size": {"type": "string", "enum": ["low", "medium", "high"]},
                    "user_location": {
                        "type": ["object", "null"],
                        "properties": {
                            "type": {"type": "string", "enum": ["approximate"]},
                            "approximate": {
                                "type": "object",
                                "properties": {
                                    "country": {"type": "string"},
                                    "region": {"type": "string"},
                                    "city": {"type": "string"},
                                    "timezone": {"type": "string"},
                                },
                            },
                        },
                    },
                },
            },
            "tools": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "required": ["type", "function"],
                    "properties": {
                        "type": {"type": "string", "enum": ["function"]},
                        "function": {
                            "type": "object",
                            "required": ["name"],
                            "properties": {
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "parameters": {"type": "object", "additionalProperties": True},
                            },
                        },
                    },
                },
            },
            "tool_choice": {
                "oneOf": [
                    {"type": "string", "enum": ["none", "auto", "required"]},
                    {
                        "type": "object",
                        "required": ["type", "function"],
                        "properties": {
                            "type": {"type": "string", "enum": ["function"]},
                            "function": {
                                "type": "object",
                                "required": ["name"],
                                "properties": {"name": {"type": "string"}},
                            },
                        },
                    },
                ]
            },
            "response_format": {
                "oneOf": [
                    {
                        "type": "object",
                        "required": ["type"],
                        "properties": {"type": {"enum": ["text"], "type": "string"}},
                    },
                    {
                        "type": "object",
                        "required": ["type"],
                        "properties": {"type": {"enum": ["json_object"], "type": "string"}},
                    },
                    {
                        "type": "object",
                        "required": ["type", "json_schema"],
                        "properties": {
                            "type": {"enum": ["json_schema"], "type": "string"},
                            "json_schema": {
                                "type": "object",
                                "required": ["name"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                    "schema": {"type": "object", "additionalProperties": True},
                                    "strict": {"type": ["boolean", "null"]},
                                },
                            },
                        },
                    },
                ]
            },
        },
        "parameters": [],
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "grok_task_retrieve": {
        "method": "POST",
        "path": "/grok/tasks",
        "operation": "task",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {"wait_seconds": 0},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "grok_tasks_retrieve_batch": {
        "method": "POST",
        "path": "/grok/tasks",
        "operation": "batch",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
            "required": ["action", "ids"],
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {"action": "retrieve_batch"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
}
