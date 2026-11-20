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


if __name__ == "__main__":
    # What settings does this model accept? No guessing needed
    models = requests.get(API + "/images/models").json()["data"]
    model = next(m for m in models if m["id"] == MODEL)
    for setting, allowed in model["supported_parameters"].items():
        print(setting, allowed.get("values", ""))

    script = json.load(open("output/script.json"))
    print(make_image(script))
