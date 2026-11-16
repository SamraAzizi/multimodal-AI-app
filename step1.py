import base64

import numpy as np
import sounddevice as sd
import soundfile as sf

from helper import call

MODEL = "openai/whisper-large-v3-turbo"
RATE = 16000  # samples per second, plenty for speech


def record(path="output/idea.wav"):
    chunks = []
    input("Press Enter and start talking...")
    # Collect audio from the mic until Enter is pressed again
    with sd.InputStream(samplerate=RATE, channels=1, callback=lambda data, *_: chunks.append(data.copy())):
        input("Recording! Press Enter to stop.")
    sf.write(path, np.concatenate(chunks), RATE)
    return path