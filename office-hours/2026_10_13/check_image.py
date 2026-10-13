import base64
from pathlib import Path

from openai import OpenAI

client = OpenAI()
image_base64 = base64.b64encode(Path("product.png").read_bytes()).decode("ascii")

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Inspect the product in this photo."},
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{image_base64}",
                },
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "visible_damage",
            "instructions": (
                "Does the product have visible damage, such as a crack, tear, or dent? "
                "Ignore shadows and damage to the packaging."
            ),
        }
    ],
)

answer = decision.answers[0]
if answer.type == "refusal":
    print(f"Refused: {answer.name}")
elif answer.type == "predicate":
    print(f"Visible damage probability: {answer.probability}")
