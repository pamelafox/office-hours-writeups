from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Review this restaurant menu."},
                {"type": "input_image", "image_url": open_image_as_data_uri("menu.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "has_vegan_option",
            "instructions": "Is there anything on this menu that is suitable for vegans?",
        }
    ],
)

print_answers(decision)
