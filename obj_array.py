from __future__ import annotations
from typing import Any
from torch import Tensor

class ObjArray:
    def __init__(self, shape: tuple[int], strides: tuple[int], offset: int, data: tuple[Any], type_string: str):
        if len(shape) != len(strides):
            raise ValueError(f"Shape and strides must have the same length")
        if offset < 0 or offset >= len(data):
            raise ValueError(f"Offset {offset} out of bounds")
        self.shape = shape
        self.strides = strides
        self.offset = offset
        self.data = data
        self.type_string = type_string

    def item(self):
        if self.shape != ():
            raise ValueError(f"Expected shape (), got {self.shape}")
        return self.data[self.offset]

    def __getitem__(self, key: int | slice | tuple[int | slice]):
        if isinstance(key, int|slice):
            return self[(key,)]
        elif isinstance(key, tuple):
            if len(key) != len(self.shape):
                raise ValueError(f"Expected {len(self.shape)} indices, got {len(key)}")
            strides = []
            shape = []
            offset = self.offset
            for k,length,s in zip(key, self.shape, self.strides):
                if isinstance(k, int):
                    offset += k * s
                elif isinstance(k, slice):
                    if k.step is not None:
                        raise ValueError("Slice steps not supported")
                    if k.start is not None or k.stop is not None:
                        raise ValueError("Slice start/stop not supported")   # TODO
                    strides.append(s)
                    shape.append(length)
                else:
                    raise ValueError(f"Invalid key {key}")
            return ObjArray(tuple(shape), tuple(strides), offset, self.data, self.type_string)
        else:
            raise ValueError(f"Invalid key {key}")

    def permute(self, dims: tuple[int]) -> ObjArray:
        if len(dims) != len(self.shape):
            raise ValueError(f"Expected {len(self.shape)} dims, got {len(dims)}")
        if set(dims) != set(range(len(dims))):
            raise ValueError(f"Invalid dims {dims}")
        strides = [self.strides[d] for d in dims]
        shape = [self.shape[d] for d in dims]
        return ObjArray(tuple(shape), tuple(strides), self.offset, self.data, self.type_string)
    
    # Can only insert 1's
    def reshape(self, shape: tuple[int]) -> ObjArray:
        if len(shape) < len(self.shape):
            raise ValueError(f"Cannot reshape to fewer dimensions")
        self_pos = 0
        strides = []
        for size in shape:
            if self_pos < len(self.shape) and size == self.shape[self_pos]:
                strides.append(self.strides[self_pos])
                self_pos += 1
            elif size == 1:
                strides.append(0)
            else:
                raise ValueError(f"Cannot reshape from {self.shape} to {shape}")
        return ObjArray(tuple(shape), tuple(strides), self.offset, self.data, self.type_string)

    def expand(self, shape: tuple[int]) -> ObjArray:
        if len(shape) != len(self.shape):
            raise ValueError(f"Expected {len(self.shape)} dims, got {len(shape)}")
        strides = []
        for size, my_size, stride in zip(shape, self.shape, self.strides):
            if my_size == 1:
                strides.append(0)
            elif my_size == size:
                strides.append(stride)
            else:
                raise ValueError(f"Cannot expand from {self.shape} to {shape}")
        return ObjArray(tuple(shape), tuple(strides), self.offset, self.data, self.type_string)

    def numel(self):
        result = 1
        for s in self.shape:
            result *= s
        return result

    def __repr__(self):
        if self.numel() <= 16:
            if len(self.shape) == 0:
                return repr(self.item())
            else:
                return '[' + ', '.join(str(ObjArray(self.shape[1:], self.strides[1:], self.offset + i * self.strides[0], self.data, self.type_string)) for i in range(self.shape[0])) + ']'
        else:
            return '...'

TensorLike = Tensor | ObjArray

def singleton_str(s: str) -> ObjArray:
    if not isinstance(s, str):
        raise ValueError(f"Expected string, got {type(s)}")
    return ObjArray((), (), 0, [s], 'str')
