from __future__ import annotations
from parse import Expr, Number, Name, Apply, Arg, Lambda, GetItem, Index, UintIndex, NameIndex, AllIndex, NamespacedName, String
from typing import Any
from torch import Tensor
import torch
import itertools

from obj_array import TensorLike, singleton_str

class Namespace:
    def __init__(self, stuff: dict[str, TensorLike | Namespace]):
        if not isinstance(stuff, dict):
            raise ValueError("Namespace must be initialized with a dict")
        for item in stuff.values():
            if not isinstance(item, TensorLike) and not isinstance(item, Namespace):
                raise ValueError("Namespace must be initialized with a dict of Tensors, ObjArrays and Namespaces")
        self.stuff = stuff

    def __getitem__(self, name: str) -> Tensor | Namespace:
        return self.stuff[name]

Value = TensorLike | Namespace
SubcellId = tuple[str, tuple[int]]

class CalculationError(Exception):
    pass

class CellInfo:
    def __init__(self, cell_id: str, subcell_dims: tuple[Option[int]]):
        self.cell_id = cell_id
        self.subcell_dims = subcell_dims

    def has_subcells(self):
        return any(d is not None for d in self.subcell_dims)

    def list_subcells(self) -> list[tuple[int]]:
        if not self.has_subcells():
            return [()]
        else:
            ranges = []
            for i, d in enumerate(self.subcell_dims):
                if d is not None:
                    ranges.append(range(d))
            return list(itertools.product(*ranges))

def get_subcell_dims(expr: Expr) -> tuple[Option[int]]:
    if isinstance(expr, Lambda):
        return tuple(_subcell_dim(d) for d in expr.args)
    else:
        return ()

def _subcell_dim(dim: Arg) -> Option[int]:
    if dim.is_subcell:
        return dim.size
    else:
        return None

def get_subcell_dim_names(expr: Expr) -> tuple[str]:
    if isinstance(expr, Lambda):
        return tuple(d.name for d in expr.args if d.is_subcell)
    else:
        return ()

def get_dependencies(expr: Expr, lambda_args: tuple[str], subcell_args: dict[str,int], cell_info: dict[str, CellInfo]) -> set[SubcellId]:
    if isinstance(expr, Number):
        return set()
    elif isinstance(expr, String):
        return set()
    elif isinstance(expr, Name):
        if expr.name in lambda_args or expr.name in subcell_args:
            return set()
        elif expr.name in cell_info:
            return {(cell_info[expr.name].cell_id, ())}
        else:
            raise CalculationError(f"Unknown name {expr.name}")
    elif isinstance(expr, NamespacedName):
        if expr.names[0] in lambda_args:
            raise CalculationError(f"Can't use lambda argument {expr.name} as a namespace")
        return {expr.names[0]}
    elif isinstance(expr, Apply):
        return set.union(*[get_dependencies(arg, lambda_args, subcell_args, cell_info) for arg in expr.args])
    elif isinstance(expr, Lambda):
        new_lambda_args = list(lambda_args)
        for arg in expr.args:
            if not arg.is_subcell and arg.name is not None:
                if arg.name in new_lambda_args or arg.name in subcell_args:
                    raise CalculationError(f"Duplicate lambda argument {arg.name}")
                new_lambda_args.append(arg.name)
        return get_dependencies(expr.expr, tuple(new_lambda_args), subcell_args, cell_info)
    elif isinstance(expr, GetItem):
        # Special case for subcell indexing.
        if isinstance(expr.expr, Name) and cell_info[expr.expr.name].has_subcells():
            result_deps = set()
            result_subcell = []
            for i, arg in enumerate(expr.indexes):
                if isinstance(arg, NameIndex):
                    if arg.name in subcell_args:
                        result_subcell.append(subcell_args[arg.name])
                elif isinstance(arg, UintIndex):
                    result_subcell.append(arg.value)
                else:
                    raise CalculationError(f"Can't use {type(arg)} as a subcell index")
                result_deps |= _get_index_dependencies(arg, lambda_args, subcell_args, cell_info)
            result_deps.add((cell_info[expr.expr.name].cell_id, tuple(result_subcell)))
            return result_deps
        else:
            return get_dependencies(expr.expr, lambda_args, subcell_args, cell_info).union(*[_get_index_dependencies(index, lambda_args, subcell_args, cell_info) for index in expr.indexes])
    else:
        raise CalculationError(f"Unknown expr kind in get_dependencies: {type(expr)}")

def _get_index_dependencies(index: Index, lambda_args: tuple[str], subcell_args: dict[str,int], cell_info: dict[str, CellInfo]) -> set[SubcellId]:
    if isinstance(index, UintIndex):
        return set()
    elif isinstance(index, NameIndex):
        if index.name in lambda_args or index.name in subcell_args:
            return set()
        else:
            return {(cell_info[index.name].cell_id, ())}
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
    def __init__(self, value: TensorLike, dims: tuple[str|int]):
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

    def named_dims(self) -> tuple[str]:
        return tuple(d for d in self.dims if isinstance(d,str))

    def swizzle_to(self, dims: list[str|int]):
        dims = tuple(dims)
        if self.dims == dims:
            return self
        my_int_dims = tuple(d for d in self.dims if isinstance(d,int))
        int_dims = tuple(d for d in dims if isinstance(d,int))
        if my_int_dims != int_dims:
            raise Exception(f"Wrong int dims: {my_int_dims} != {int_dims}")
        if set(self.dims) != set(dims):
            raise Exception(f"Args {self.dims} is not a permutation of {dims}")
        if len(self.dims) != len(dims):
            raise Exception(f"This shouldn't happen. Dimension count mismatch. {self.dims}, {dims}")
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
        if len(pdims) < len(self.dims):
            raise Exception(f"This shouldn't happen. Not all dims are present. {self.dims}, {dims}, {pdims}")
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


def calculate(expr: Expr, env: dict[str|SubCellId, Value], cell_info: dict[str, CellInfo], subcell: tuple[int]) -> CalcResult:
    if isinstance(expr, Number):
        return CalcResult(torch.tensor(expr.value, dtype=torch.float32), ())
    elif isinstance(expr, String):
        return CalcResult(singleton_str(expr.value), ())
    elif isinstance(expr, Name):
        if expr.name in cell_info:
            key = cell_info[expr.name].cell_id, ()
        elif expr.name in env:
            key = expr.name
        else:
            raise CalculationError(f"Unknown name {expr.name}")

        result = env[key]
        if isinstance(result, Arg):
            if result.size is None:
                raise CalculationError(f"Require argument size for {result.name}")
            t = torch.arange(0, result.size, dtype=torch.float32)
            return CalcResult(t, (result.name,))
        elif isinstance(result, Tensor):
            return CalcResult(result, tuple(range(len(result.shape))))
        elif isinstance(result, Namespace):
            raise CalculationError("Cannot return bare namespace")
        else:
            raise Exception(f"Unrecognized type of value: {type(result)}")
    elif isinstance(expr, NamespacedName):
        try:
            result = env[expr.names[0]]
            for name in expr.names[1:]:
                result = result[name]
            if isinstance(result, Tensor):
                return CalcResult(result, tuple(range(len(result.shape))))
            elif isinstance(result, Namespace):
                raise CalculationError("Cannot return bare namespace")
            else:
                raise Exception(f"Unrecognized type of value found in namespace: {type(result)}")
        except KeyError as e:
            raise CalculationError(f"Unknown namespaced value: {expr}") from e
    elif isinstance(expr, Apply):
        args,dims = swizzle_and_broadcast([calculate(arg, env, cell_info, ()) for arg in expr.args])
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
        subcell_i = 0
        dims = []
        sizes = {}
        for pos, arg in enumerate(expr.args):
            if arg.is_subcell:
                if subcell_i >= len(subcell):
                    raise CalculationError(f"Too many subcells in lambda")
                new_env[arg.name] = torch.tensor(subcell[subcell_i], dtype=torch.int32)
                subcell_i += 1
            elif arg.name != None:
                if arg.name in new_env:
                    raise CalculationError(f"Arg name conflict: {arg.name}")
                new_env[arg.name] = arg
                dims.append(arg.name)
                if arg.size != None:
                    sizes[arg.name] = arg.size
            else:
                dims.append(num_unnamed_args)
                num_unnamed_args += 1
        result = calculate(expr.expr, new_env, cell_info, ())
        old_dims = tuple(d for d in result.named_dims() if (d,()) in env)
        dims = tuple(dims)
        return result.swizzle_and_broadcast_maybe_missing_sizes(old_dims + dims, sizes).anonymize(dims)
    elif isinstance(expr, GetItem):
        return calculate(expr.expr, env, cell_info, ()).get_item(expr.indexes)
    else:
        raise CalculationError(f"Unknown expr kind: {type(expr)}")

