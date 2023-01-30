import torch

from obj_array import TensorLike, ObjArray

def tensorlike_to_str(t: TensorLike) -> str:
    if isinstance(t, ObjArray):
        return str(t)
    if t.shape == ():
        return str(t.item())
    # Don't print entire tensor if there's more than 16 elements
    elif t.numel() <= 16:
        return str(t.tolist())
    else:
        return f'...{", ".join(str(e.item()) for e in t.flatten()[:8])}...'

def dtype_to_str(dtype: torch.dtype) -> str:
    if dtype == torch.float32:
        return 'f32'
    else:
        raise ValueError(f'Unknown dtype {dtype}')

def type_to_str(t: TensorLike) -> str:
    if isinstance(t, ObjArray):
        type_str = t.type_string
    else:
        type_str = dtype_to_str(t.dtype)
    if t.shape == ():
        return type_str
    else:
        return f'[{", ".join([str(d) for d in t.shape])}] -> {type_str}'
