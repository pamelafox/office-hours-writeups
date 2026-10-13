from openai import OpenAI

from image_utils import open_image_as_data_uri, print_answers

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Analyze this graph of tree cover loss by climate zone."},
                {"type": "input_image", "image_url": open_image_as_data_uri("tree_cover_loss.png")},
            ],
        }
    ],
    questions=[
        {
            "type": "choice",
            "name": "zone_losing_most_trees",
            "instructions": "Which zone is losing the most trees?",
            "choices": [
                {"value": "tropical"},
                {"value": "subtropical"},
                {"value": "temperate"},
                {"value": "boreal"},
            ],
        }
    ],
)

print_answers(decision)
