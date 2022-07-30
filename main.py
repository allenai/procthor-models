import os

checkpoints = {
    "10-house-ablation": "scale_ablation/exp_10-houses__stage_00__steps_000005000608.pt",
    "100-house-ablation": "scale_ablation/exp_100-houses__stage_00__steps_000117661834.pt",
    "1000-house-ablation": "scale_ablation/exp_1000-houses__stage_02__steps_000160070274.pt",
    "10k-house-ablation": "scale_ablation/exp_10k-houses__stage_02__steps_000195225491.pt",
}


def load_checkpoint(checkpoint: str) -> dict:
    if checkpoint not in checkpoints:
        raise ValueError(f"Checkpoint ({checkpoint}) not found in {checkpoints.keys()}")
    return os.path.join(os.path.dirname(__file__), checkpoints[checkpoint])
