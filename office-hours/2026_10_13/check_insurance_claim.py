from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Claim states that this damage is due to hail."},
                {"type": "input_image", "image_url": open_image_as_data_uri("dented_car.jpg")},
            ],
        },
    ],
    questions=[
        {
            "type": "predicate",
            "name": "hail_claim_valid",
            "instructions": (
                "You help auto insurance companies process claims. Judge the cause of the car damage in the photo "
                "and the validity of the claim. Is the damage consistent with hail, making the claim valid?"
            ),
        }
    ],
)

print_answers(decision)
