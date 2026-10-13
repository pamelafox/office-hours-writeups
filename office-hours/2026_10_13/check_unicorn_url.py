import base64
import urllib.request

from openai import OpenAI

from image_utils import print_answers

IMAGE_URL = "https://raw.githubusercontent.com/Azure-Samples/openai-chat-vision-quickstart/main/notebooks/ur.jpg"

# The Decisions API only accepts inline data URLs, so fetch the image and encode it.
with urllib.request.urlopen(IMAGE_URL) as response:
    image_base64 = base64.b64encode(response.read()).decode("ascii")

client = OpenAI()

decision = client.decisions.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Inspect the animal in this image."},
                {"type": "input_image", "image_url": f"data:image/jpeg;base64,{image_base64}"},
            ],
        }
    ],
    questions=[
        {
            "type": "predicate",
            "name": "is_unicorn",
            "instructions": "Is this a unicorn?",
        }
    ],
)

print_answers(decision)
