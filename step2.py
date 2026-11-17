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