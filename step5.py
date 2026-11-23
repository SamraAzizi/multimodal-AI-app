import base64
import json
import time

import requests

from helper import HEADERS, add_cost, post

MODEL = "google/veo-3.1"


def make_video(script, image_path):
    # Turn the cover image into text so it can go inside the JSON request
    image = base64.b64encode(open(image_path, "rb").read()).decode()

    # Step 1: submit the job. We get back a job ID right away, not the video.
    job = post("/videos", {
        "model": MODEL,
        "prompt": script["video_prompt"],
        "duration": 8,  # Veo 3.1 allows 4, 6 or 8
        "resolution": "720p",
        # Optional: remove frame_images to generate the video from the prompt alone
        "frame_images": [{
            "type": "image_url",
            "image_url": {"url": "data:image/png;base64," + image},
            "frame_type": "first_frame",  # the clip starts on our cover image
        }],
    }).json()