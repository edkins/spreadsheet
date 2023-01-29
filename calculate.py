from parse import Expr, Number, Name, Apply
from typing import Any

class CalculationError(Exception):
    pass

def calculate(expr: Expr) -> Any:
    if isinstance(expr, Number):
        return expr.value
    elif isinstance(expr, Name):
        raise CalculationError("Cannot calculate names yet")
    elif isinstance(expr, Apply):
        if expr.func == "+":
            return calculate(expr.args[0]) + calculate(expr.args[1])
        elif expr.func == "-":
            return calculate(expr.args[0]) - calculate(expr.args[1])
        elif expr.func == "*":
            return calculate(expr.args[0]) * calculate(expr.args[1])
        elif expr.func == "/":
            return calculate(expr.args[0]) / calculate(expr.args[1])
        else:
            raise CalculationError(f"Unknown function {expr.func}")
    else:
        raise CalculationError(f"Unknown expr kind")
