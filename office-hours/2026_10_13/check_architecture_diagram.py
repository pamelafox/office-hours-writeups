from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Check whether this image needs alt text for accessibility."},
                {"type": "input_image", "image_url": open_image_as_data_uri("azure_arch.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "is_architecture_diagram",
            "instructions": "Is this a cloud architecture diagram that shows connected services?",
        },
        {
            "type": "predicate",
            "name": "needs_alt_text",
            "instructions": "Does this image convey information that a screen reader user would miss without alt text?",
        },
    ],
)

print_answers(decision)
