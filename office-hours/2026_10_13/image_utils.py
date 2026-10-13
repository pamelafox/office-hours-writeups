import base64
import mimetypes
from pathlib import Path


def open_image_as_data_uri(filename):
    mime_type = mimetypes.guess_type(filename)[0] or "image/png"
    image_base64 = base64.b64encode(Path(filename).read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{image_base64}"


def print_answers(decision):
    for answer in decision.answers:
        if answer.type == "refusal":
            print(f"Refused: {answer.name}")
        elif answer.type == "predicate":
            print(f"{answer.name}: probability {answer.probability}")
        elif answer.type == "choice":
            print(f"{answer.name}: {answer.choice} (confidence {answer.confidence})")
            for p in answer.probabilities:
                print(f"  {p.value}: {p.probability}")
