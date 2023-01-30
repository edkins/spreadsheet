from torch import Tensor
import torch

def tensor_to_str(t: Tensor) -> str:
    if t.shape == ():
        return str(t.item())
    # Don't print entire tensor if there's more than 16 elements
    elif t.numel() <= 16:
        return str(t.tolist())
    else:
        return f'[{", ".join([str(d) for d in t.shape])}] -> {dtype_to_str(t.dtype)} {t.flatten()[:8].tolist()}...'

def dtype_to_str(dtype: torch.dtype) -> str:
    if dtype == torch.float32:
        return 'f32'
    else:
        raise ValueError(f'Unknown dtype {dtype}')

def type_to_str(t: Tensor) -> str:
    if t.shape == ():
        return dtype_to_str(t.dtype)
    else:
        return f'[{", ".join([str(d) for d in t.shape])}] -> {dtype_to_str(t.dtype)}'
