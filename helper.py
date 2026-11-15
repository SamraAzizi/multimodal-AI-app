import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()
API = "https://openrouter.ai/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"}
os.makedirs("output", exist_ok=True)

costs = {}  # running total: "step (model)" -> cost in USD


def post(path, payload):
    response = requests.post(API + path, headers=HEADERS, json=payload)
    if not response.ok:
        raise Exception(response.text)
    return response


def add_cost(step, model, cost):
    costs[f"{step} ({model})"] = cost
    print(f"{step} ({model}): ${cost:.4f}")


def call(step, path, payload):
    """Send a request and add its usage.cost to the running total."""
    data = post(path, payload).json()
    add_cost(step, data.get("model", payload.get("model")), data["usage"]["cost"])
    return data


def lookup_cost(generation_id):
    """For responses with no JSON body (like audio), look the cost up by ID."""
    while True:
        response = requests.get(API + "/generation", headers=HEADERS, params={"id": generation_id})
        if response.ok:
            return response.json()["data"]["total_cost"]
        time.sleep(2)  # takes a few seconds to show up

