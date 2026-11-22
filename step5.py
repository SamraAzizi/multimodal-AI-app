import base64
import json
import time

import requests

from helper import HEADERS, add_cost, post

MODEL = "google/veo-3.1"


def make_video(script, image_path):
    # Turn the cover image into text so it can go inside the JSON request
    image = base64.b64encode(open(image_path, "rb").read()).decode()
