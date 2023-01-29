from parse import Expr, Number, Name, Apply
from typing import Any
from torch import Tensor
import torch

class CalculationError(Exception):
    pass

def get_dependencies(expr: Expr) -> set[str]:
    if isinstance(expr, Number):
        return set()
    elif isinstance(expr, Name):
        return {expr.name}
    elif isinstance(expr, Apply):
        return set.union(*map(get_dependencies, expr.args))
    else:
        raise CalculationError(f"Unknown expr kind")

def calculate(expr: Expr, env: dict[str, Tensor]) -> Tensor:
    if isinstance(expr, Number):
        return torch.tensor(expr.value, dtype=torch.float32)
    elif isinstance(expr, Name):
        if expr.name not in env:
            raise CalculationError(f"Unknown cell: {expr.name}")
        return env[expr.name]
    elif isinstance(expr, Apply):
        lhs = calculate(expr.args[0], env)
        rhs = calculate(expr.args[1], env)
        if lhs.shape != rhs.shape:
            raise CalculationError(f"Shapes don't match: {lhs.shape} vs {rhs.shape}")
        if expr.func == '+':
            return lhs + rhs
        elif expr.func == '-':
            return lhs - rhs
        elif expr.func == '*':
            return lhs * rhs
        elif expr.func == '/':
            return lhs / rhs
        else:
            raise CalculationError(f"Unknown function {expr.func}")
    else:
        raise CalculationError(f"Unknown expr kind")
