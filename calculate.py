from parse import Expr, Number, Name, Apply
from typing import Any
from value import Value, singleton_float

class CalculationError(Exception):
    pass

def calculate(expr: Expr, env: dict[str, Value]) -> Value:
    if isinstance(expr, Number):
        return singleton_float(expr.value)
    elif isinstance(expr, Name):
        if expr.name not in env:
            raise CalculationError(f"Unknown cell: {expr.name}")
        return env[expr.name]
    elif isinstance(expr, Apply):
        lhs = calculate(expr.args[0], env)
        rhs = calculate(expr.args[1], env)
        if expr.func in ['+', '-', '*', '/']:
            return lhs.scalar_builtin(expr.func, rhs)
        else:
            raise CalculationError(f"Unknown function {expr.func}")
    else:
        raise CalculationError(f"Unknown expr kind")
