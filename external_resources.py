from transformer_lens import HookedTransformer
import re
import torch

from calculate import Namespace
from display import type_to_str

re_name = re.compile(r'^[a-zA-Z0-9_]+$')

external_resource_dict = {}

class ImportError(Exception):
    pass

def neelify(name):
    return name.replace('_', '-')

def load_external_resource(name: str) -> Namespace:
    if not re_name.match(name):
        raise ValueError('Invalid external resource name')

    name = neelify(name)
    print("Attempting to load external resource", name)
    try:
        transformer = HookedTransformer.from_pretrained(name, device='cpu')
    except ValueError as e:
        raise ImportError(f'Could not load external resource: {name}') from e

    params = {
            'embed': {},
            'pos_embed': {},
            'attn': {},
            'mlp': {},
            'unembed': {},
            'cfg': {},
    }
    for name, param in transformer.named_parameters():
        value = param.detach()
        if not isinstance(value, torch.Tensor) or value.dtype != torch.float32:
            raise ImportError(f'Could not load external resource: {name} is not an f32 tensor')
        split = name.split('.')
        try:
            if split[0] == 'blocks':
                layer = int(split[1])
                split = split[2:]
                if len(split) != 2:
                    raise ImportError(f'Unexpected parameter name in import: {name}')
                if split[1] not in params[split[0]]:
                    params[split[0]][split[1]] = torch.zeros((transformer.cfg.n_layers, *value.shape))
                params[split[0]][split[1]][layer] = value
            else:
                if len(split) != 2:
                    raise ImportError(f'Unexpected parameter name in import: {name}')
                params[split[0]][split[1]] = value
        except KeyError as e:
            raise ImportError(f'Unexpected parameter name in import: {name}') from e

    cfg = transformer.cfg.to_dict()
    for key in ['n_layers', 'd_model', 'n_ctx', 'd_head', 'n_heads', 'd_mlp', 'd_vocab']:
        params['cfg'][key] = torch.tensor(cfg[key], dtype=torch.float32)

    for p0 in params:
        for p1 in params[p0]:
            print(f'm::{p0}::{p1} : {type_to_str(params[p0][p1])}')
    return Namespace({p0: Namespace(stuff) for p0, stuff in params.items()})

def get_external_resource(name: str) -> Namespace:
    if name not in external_resource_dict:
        external_resource_dict[name] = load_external_resource(name)
    return external_resource_dict[name]
