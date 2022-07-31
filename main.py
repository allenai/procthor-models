import json
import os


def load_model(model: str) -> str:
    with open("models.json", "r") as f:
        models = json.load(f)

    if model not in models:
        raise ValueError(f"Model ({model}) not found in {models.keys()}")

    return os.path.join(os.path.dirname(__file__), models[model])
