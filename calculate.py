from parse import Expr, Number, Name, Apply, Arg, Lambda, GetItem, Index, UintIndex, NameIndex, AllIndex
from typing import Any
from torch import Tensor
import torch

class CalculationError(Exception):
    pass

def get_dependencies(expr: Expr, lambda_args: tuple[str] = ()) -> set[str]:
    if isinstance(expr, Number):
        return set()
    elif isinstance(expr, Name):
        if expr.name in lambda_args:
            return set()
        else:
            return {expr.name}
    elif isinstance(expr, Apply):
        return set.union(*[get_dependencies(arg, lambda_args) for arg in expr.args])
    elif isinstance(expr, Lambda):
        new_args = lambda_args + tuple(arg.name for arg in expr.args if arg.name is not None)
        return get_dependencies(expr.expr, new_args)
    elif isinstance(expr, GetItem):
        return get_dependencies(expr.expr, lambda_args).union(*[get_index_dependencies(index, lambda_args) for index in expr.indexes])
    else:
        raise CalculationError(f"Unknown expr kind in get_dependencies: {type(expr)}")

def get_index_dependencies(index: Index, lambda_args: tuple[str]) -> set[str]:
    if isinstance(index, UintIndex):
        return set()
    elif isinstance(index, NameIndex):
        if index.name in lambda_args:
            return set()
        else:
            return {index.name}
    elif isinstance(index, AllIndex):
        return set()
    else:
        raise CalculationError(f"Unknown index kind in get_index_dependencies: {type(index)}")

# For each dimension of the result, we store the corresponding arg name.
# This will be an integer if the dimension is not an arg.
# The integers always count from 0 and are in the right order.
#
# For example:
# [i,j] -> x[j,i]
#     Then the args will be ('j', 'i')
# [i,j] -> y[i, :, j]
#     Then the args will be ('i', 0, 'j')

class CalcResult:
    def __init__(self, value: Tensor, dims: tuple[str|int]):
        if any(d is None for d in dims):
            raise Exception("None in dims")
        if len(dims) != len(value.shape):
            raise CalculationError(f"Wrong number of dims: {len(dims)} != {len(value.shape)}")
        int_dims = tuple(d for d in dims if isinstance(d,int))
        if int_dims != tuple(range(len(int_dims))):
            raise CalculationError(f"Unnamed dims must be in order. Got {int_dims}")
        if len(set(dims)) != len(dims):
            raise CalculationError(f"Duplicate dims in {dims}")
        self.value = value
        self.dims = dims

    def count_unnamed_dims(self):
        int_dims = tuple(d for d in self.dims if isinstance(d,int))
        return len(int_dims)

    def swizzle_to(self, dims: list[str|int]):
        dims = tuple(dims)
        if self.dims == dims:
            return self
        my_int_dims = tuple(d for d in self.dims if isinstance(d,int))
        int_dims = tuple(d for d in dims if isinstance(d,int))
        if my_int_dims != int_dims:
            raise CalculationError(f"Wrong int dims: {my_int_dims} != {int_dims}")
        if set(self.dims) != set(dims):
            raise CalculationError(f"Args {self.dims} is not a permutation of {dims}")
        if len(self.dims) != len(dims):
            raise CalculationError("This shouldn't happen. Dimension count mismatch.")
        permutation = tuple(map(lambda x: self.dims.index(x), dims))
        return CalcResult(self.value.permute(permutation), dims)

    def broadcast_to(self, dims: list[str|int], sizes: dict[str, int]):
        if self.dims == dims:
            return self
        shape = []
        shape2 = []
        for dim in dims:
            if dim in sizes:
                shape2.append(sizes[dim])
            else:
                raise CalculationError(f"Unknown size for dim {dim}")

            if dim in self.dims:
                d = self.dims.index(dim)
                shape.append(self.value.shape[d])
                if self.value.shape[d] != sizes[dim]:
                    raise CalculationError(f"Wrong size for dim {dim}: {self.value.shape[d]} != {sizes[dim]}")
            else:
                shape.append(1)

        reshaped = self.value.reshape(shape)
        expanded = reshaped.expand(shape2)
        return CalcResult(expanded, dims)

    def swizzle_and_broadcast_to(self, dims: list[str|int], sizes: dict[str, int]):
        pdims = [d for d in dims if d in self.dims]
        return self.swizzle_to(pdims).broadcast_to(dims, sizes)

    # A more tolerant version that will infer sizes from existing dims where possible.
    def swizzle_and_broadcast_maybe_missing_sizes(self, dims: list[str|int], sizes: dict[str, int]):
        new_sizes = dict(sizes)
        for d, dim in enumerate(self.dims):
            my_size = self.value.shape[d]
            if dim in new_sizes:
                if new_sizes[dim] != my_size:
                    raise CalculationError(f"Wrong size for dim {dim}: {new_sizes[dim]} != {my_size}")
            else:
                new_sizes[dim] = my_size

        if self.count_unnamed_dims() != len([d for d in dims if isinstance(d,int)]):
            raise CalculationError(f"Wrong number of unnamed dims: {self.count_unnamed_dims()} != {len([d for d in dims if isinstance(d,int)])}")
        return self.swizzle_and_broadcast_to(dims, new_sizes)

    # Convert the given named and unnamed dimensions to unnamed dimensions
    # in the correct order.
    def anonymize(self, dims: list[str|int]):
        new_dims = []
        num_unnamed = 0
        for dim in self.dims:
            if isinstance(dim, int):
                new_dims.append(num_unnamed)
                num_unnamed += 1
            elif dim in dims:
                new_dims.append(num_unnamed)
                num_unnamed += 1
            else:
                new_dims.append(dim)
        return CalcResult(self.value, new_dims)

    def get_item(self, indexes: tuple[Index]):
        if len(indexes) == 0:
            raise CalculationError("Can't get item with no indexes")
        if self.count_unnamed_dims() != len(indexes):
            raise CalculationError(f"Wrong number of indexes {len(indexes)} for {self.count_unnamed_dims()}")

        py_indexes = []
        resulting_dims = []
        d = 0
        d_out = 0
        for d_self, dim in enumerate(self.dims):
            if isinstance(dim, str):
                py_indexes.append(slice(None))
                resulting_dims.append(dim)
            elif isinstance(dim, int):
                index = indexes[d]
                d += 1
                if isinstance(index, UintIndex):
                    if index.value < 0 or index.value >= self.value.shape[d_self]:
                        raise CalculationError(f"Index {index.value} out of range")
                    py_indexes.append(index.value) # No resulting dim here
                elif isinstance(index, NameIndex):
                    py_indexes.append(slice(None))
                    resulting_dims.append(index.name)
                elif isinstance(index, AllIndex):
                    py_indexes.append(slice(None))
                    resulting_dims.append(d_out)
                    d_out += 1
                else:
                    raise Exception("Unrecognized kind of index")
            else:
                raise Exception("Dims must be str or int")

        if len(set(resulting_dims)) != len(resulting_dims):
            raise CalculationError(f"Currently unsupported: repeated dimensions in indexing (diagonal extraction)")  # TODO

        if len(py_indexes) == 1:
            result = self.value[py_indexes[0]]
        else:
            result = self.value[tuple(py_indexes)]

        if len(result.shape) != len(resulting_dims):
            raise Exception(f"Dim mismatch in get_item: {result.shape} vs {resulting_dims}")
        return CalcResult(result, resulting_dims)

# Given a collection of CalcResults, we want to rejig the dimensions
# so that they all match up.
# This means:
#   - named dimensions must match
#   - unnamed dimensions must be in the same order (we don't reorder these, and they must be equal in number)
# We also assert that the corresponding dimensions are the same size.
# The first CalcResult has "priority" when it comes to deciding the order.
def swizzle_and_broadcast(params: list[CalcResult]) -> tuple[list[Tensor], list[str|int]]:
    if len(params) == 0:
        return [], []
    if len(params) == 1:
        return [params[0].value], params[0].dims

    # First, we need to work out the order of the dimensions.
    # We do this by looking at the first param, and then adding information
    # from the other params.
    dims = []
    num_unnamed = params[0].count_unnamed_dims()
    sizes = {}
    for other in params:
        if other.count_unnamed_dims() != num_unnamed:
            raise CalculationError(f"Unnamed dimensions don't match {num_unnamed} vs {other.count_unnamed_dims()}")
        for d,dim in enumerate(other.dims):
            if dim not in dims:
                dims.append(dim)
            if dim in sizes:
                if sizes[dim] != other.value.shape[d]:
                    raise CalculationError(f"Dimension {dim} has different sizes")
            else:
                sizes[dim] = other.value.shape[d]

    results = [param.swizzle_and_broadcast_to(dims, sizes) for param in params]
    # Check the dimensions match.
    for other in results[1:]:
        if results[0].value.shape != other.value.shape:
            raise CalculationError(f"Dimensions don't match {results[0].value.shape} vs {other.value.shape}")
        if results[0].dims != other.dims:
            raise CalculationError(f"Dimensions don't match {results[0].dims} vs {other.dims}")
    return [r.value for r in results], results[0].dims


def calculate(expr: Expr, env: dict[str, Tensor]) -> CalcResult:
    if isinstance(expr, Number):
        return CalcResult(torch.tensor(expr.value, dtype=torch.float32), ())
    elif isinstance(expr, Name):
        if expr.name not in env:
            raise CalculationError(f"Unknown cell: {expr.name}")
        result = env[expr.name]
        if isinstance(result, Arg):
            if result.size is None:
                raise CalculationError(f"Require argument size for {result.name}")
            t = torch.arange(0, result.size, dtype=torch.float32)
            return CalcResult(t, (result.name,))
        else:
            return CalcResult(result, tuple(range(len(result.shape))))
    elif isinstance(expr, Apply):
        args,dims = swizzle_and_broadcast([calculate(arg, env) for arg in expr.args])
        if expr.func == '+':
            return CalcResult(args[0] + args[1], dims)
        elif expr.func == '-':
            return CalcResult(args[0] - args[1], dims)
        elif expr.func == '*':
            return CalcResult(args[0] * args[1], dims)
        elif expr.func == '/':
            return CalcResult(args[0] / args[1], dims)
        else:
            raise CalculationError(f"Unknown function {expr.func}")
    elif isinstance(expr, Lambda):
        new_env = dict(env)
        num_unnamed_args = 0
        dims = []
        sizes = {}
        for pos, arg in enumerate(expr.args):
            if arg.name != None:
                if arg.name in new_env:
                    raise CalculationError(f"Arg name conflict: {arg.name}")
                new_env[arg.name] = arg
                dims.append(arg.name)
                if arg.size != None:
                    sizes[arg.name] = arg.size
            else:
                dims.append(num_unnamed_args)
                num_unnamed_args += 1
        return calculate(expr.expr, new_env).swizzle_and_broadcast_maybe_missing_sizes(dims, sizes).anonymize(dims)
    elif isinstance(expr, GetItem):
        return calculate(expr.expr, env).get_item(expr.indexes)
    else:
        raise CalculationError(f"Unknown expr kind: {type(expr)}")

