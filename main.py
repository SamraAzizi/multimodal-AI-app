from helper import costs
from step1 import record, transcribe
from step2 import write_script
from step3 import make_image
from step4 import speak
from step5 import make_video


def print_cost_receipt():
    print("\nCOST RECEIPT")
    for step, cost in costs.items():
        print(f"{step:<55} ${cost:.4f}")