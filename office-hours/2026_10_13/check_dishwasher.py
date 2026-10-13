from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "I want to wash the dishes quickly. Look at this dishwasher panel."},
                {"type": "input_image", "image_url": open_image_as_data_uri("dishwasher.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "has_quick_wash_option",
            "instructions": "Does this dishwasher have a quick or express wash option that is visible on the panel?",
        }
    ],
)

print_answers(decision)
