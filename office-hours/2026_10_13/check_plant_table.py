from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Analyze this plant price table."},
                {"type": "input_image", "image_url": open_image_as_data_uri("page_0.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "has_plant_under_10",
            "instructions": "Is there any plant in the table priced under $10?",
        }
    ],
)

print_answers(decision)
