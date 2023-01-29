import torch
from typing import Optional

class Value:
    pass

class UnknownValue(Value):
    def __init__(self):
        pass

    @property
    def complete(self):
        return False

    @property
    def dims(self) -> Optional[tuple[int]]:
        return None

    @property
    def type_string(self) -> str:
        return ''

    def __eq__(self, other):
        return isinstance(other, UnknownValue)

    def __ne__(self, other):
        return not self.__eq__(other)

    def scalar_builtin(self, f: str, other: Value):
        return self

    def __repr__(self):
        return 'Unknown'

class TypedValue(Value):
    def __init__(self, value: torch.Tensor, mask: torch.Tensor):
        if value.shape != mask.shape:
            raise ValueError('Value and mask must have the same shape')
        if value.dtype != torch.float32:
            raise ValueError('Value must be float32')
        self.value = value
        self.mask = mask

    @property
    def complete(self):
        return self.mask.all().item()

    @property
    def dims(self) -> Optional[tuple[int]]:
        return self.value.shape

    def __repr__(self):
        if self.complete:
            if len(self.dims) == 0:
                return repr(self.value.item())
            else:
                return repr(self.value)
        else:
            if len(self.dims) == 0:
                return 'IncompleteF32'
            else:
                return f'Incomplete({repr(self.mask)}, {repr(self.value)})'

    @property
    def type_string(self) -> str:
        return '[' + ', '.join([str(d) for d in self.dims]) + '] -> f32'

    def __eq__(self, other):
        if not isinstance(other, TypedValue):
            return False
        if self.dims != other.dims:
            return False
        return ((self.value == other.value) & (self.mask == other.mask)).all().item()

    def __ne__(self, other):
        return not self.__eq__(other)

    def scalar_builtin(self, f: str, other: Value):
        if isinstance(other, UnknownValue):
            return other
        if other.dims != self.dims:
            # TODO: broadcast
            raise ValueError('Value and mask must have the same shape')
        if f == '+':
            return TypedValue(self.value + other.value, self.mask & other.mask)
        elif f == '-':
            return TypedValue(self.value - other.value, self.mask & other.mask)
        elif f == '*':
            return TypedValue(self.value * other.value, self.mask & other.mask)
        elif f == '/':
            return TypedValue(self.value / other.value, self.mask & other.mask)
        else:
            raise ValueError(f'Invalid scalar builtin: {f}')

def singleton_float(value):
    return TypedValue(torch.tensor(value, dtype=torch.float32), torch.tensor(True))

