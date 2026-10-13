import sys
from openai import OpenAI

path = sys.argv[1] if len(sys.argv) > 1 else "test_120k_tokens.txt"
with open(path, encoding="utf-8") as f:
    text = f.read()

client = OpenAI()
decision = client.decisions.create(
    model="gpt-6-luna",
    input=text,
    questions=[
        {
            "type": "predicate",
            "instructions": "Mochi the cat is relaxed and comfortable."
        }
    ],
)
print(decision)
