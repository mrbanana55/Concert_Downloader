from models import Concert
import json

def load_concert(path: str) -> Concert:
    with open(path) as f:
        data = json.load(f)
    return Concert(**data)