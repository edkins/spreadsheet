from torch import Tensor

def tensor_to_str(t: Tensor) -> str:
    if t.shape == ():
        return str(t.item())
    else:
        return str(t.tolist())
