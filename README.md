# ProcTHOR Models

Model weights for ProcTHOR experiments. The full list of models is available in [models.json](https://github.com/allenai/procthor-models/blob/main/models.json).

## Example

To load the models, use the prior package:
```python
import prior
model_path = prior.load_model(project="procthor-models", model="object-nav-pretraining")

import torch
torch.load(model_path)
```

More information about how to use them will be available soon!

## Models

Habitat Baseline

> **Warning**
> For the Habitat baseline, the order of the objects for the `GoalObjectTypeThorSensor` is not sorted (as it typically is in AllenAct), and is as follows:

```
{
    "Chair": 0,
    "Bed": 1,
    "HousePlant": 2,
    "Toilet": 3,
    "Television": 4,
    "Sofa": 5,
}
```
