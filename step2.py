import json

from helper import call

# Free to follow along: ["openrouter/free"]
MODELS = ["openai/gpt-6.1-sol", "google/gemini-3.8-flash"]  # the second is a fallback

PROMPT = "Turn this voice note into a short video.\n\nVoice note: "

# The exact shape we want back. The model has to fill in these three fields.
SCHEMA = {
    "type": "object",
    "properties": {
        "script": {"type": "string", "description": "A 40 to 60 word voiceover, with audio tags like [excited] or [whispers]"},
        "image_prompt": {"type": "string", "description": "A detailed prompt for a 16:9 cover image"},
        "video_prompt": {"type": "string", "description": "An 8 second clip that starts on the cover image: describe the motion"},
    },
    "required": ["script", "image_prompt", "video_prompt"],
    "additionalProperties": False,
}


def write_script(text):
    data = call("Script", "/chat/completions", {
        "models": MODELS,  # if the first model is down, OpenRouter tries the next
        "messages": [{"role": "user", "content": PROMPT + text}],
        "response_format": {
            "type": "json_schema",
            "json_schema": {"name": "video_plan", "strict": True, "schema": SCHEMA},
        },
        "provider": {"require_parameters": True},  # only use providers that support the schema
    })
    return json.loads(data["choices"][0]["message"]["content"])


if __name__ == "__main__":
    text = open("output/transcript.txt", encoding="utf-8").read()
    script = write_script(text)
    print(json.dumps(script, indent=2))
    json.dump(script, open("output/script.json", "w"), indent=2)
