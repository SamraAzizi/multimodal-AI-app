import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()
API = "https://openrouter.ai/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"}
os.makedirs("output", exist_ok=True)

costs = {}  # running total: "step (model)" -> cost in USDs