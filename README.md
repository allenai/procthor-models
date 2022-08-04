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
