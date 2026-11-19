import base64
import json

import requests

from helper import API, call

MODEL = "google/gemini-3.1-flash-image"


def make_image(script):
    data = call("Image", "/images", {
        "model": MODEL,
        "prompt": script["image_prompt"],
        "aspect_ratio": "16:9",
    })
    # JSON can only carry text, so the image comes back as base64 text.
    # Decoding turns that text back into the real image bytes, which we save as a PNG.
    image_text = data["data"][0]["b64_json"]
    image_bytes = base64.b64decode(image_text)
    open("output/cover.png", "wb").write(image_bytes)
    return "output/cover.png"