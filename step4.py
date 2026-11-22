import json

import numpy as np
import soundfile as sf

from helper import add_cost, lookup_cost, post

MODEL = "google/gemini-3.1-flash-tts-preview"


def speak(script):
    response = post("/audio/speech", {
        "model": MODEL,
        "input": script["script"],
        "voice": "Puck",
    })

    # Gemini sends raw PCM audio, which won't play on its own, so save it as a WAV
    audio = np.frombuffer(response.content, dtype=np.int16)
    sf.write("output/voiceover.wav", audio, 24000)

    add_cost("Voiceover", MODEL, lookup_cost(response.headers["X-Generation-Id"]))
    return "output/voiceover.wav"


if __name__ == "__main__":
    script = json.load(open("output/script.json"))
    print(speak(script))
