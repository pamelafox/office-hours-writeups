from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Identify the reptiles in this photo."},
                {"type": "input_image", "image_url": open_image_as_data_uri("mystery_reptile.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "choice",
            "name": "reptile_type",
            "instructions": "Are the reptiles alligators or crocodiles?",
            "choices": [
                {"value": "alligator", "description": "Broad U-shaped snout, upper jaw hides lower teeth."},
                {"value": "crocodile", "description": "Narrow V-shaped snout, lower teeth visible when mouth closed."},
                {"value": "other", "description": "Neither, or not reptiles."},
            ],
        }
    ],
)

print_answers(decision)

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Identify the reptiles in this photo."},
                {"type": "input_image", "image_url": open_image_as_data_uri("mystery_reptile.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "is_alligator",
            "instructions": "Are the reptiles alligators (rather than crocodiles)?",
        },
        {
            "type": "predicate",
            "name": "is_crocodile",
            "instructions": "Are the reptiles crocodiles (rather than alligators)?",
        },
    ],
)

print_answers(decision)
