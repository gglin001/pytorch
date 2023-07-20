from typing import List
import torch
import torch._dynamo
import torch._dynamo.config
import logging

# logging.basicConfig(format="%(message)s")
torch._logging.set_logs(all=logging.DEBUG)
torch._logging.set_logs(dynamo=logging.DEBUG)


def my_compiler(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
    print("my_compiler() called with FX graph:")
    # gm.graph.print_tabular()
    return gm.forward


@torch.compile(backend=my_compiler)
def toy_example(a, b):
    x = a / (torch.abs(a) + 1)
    if b.sum() < 0:
        b = b * -1
    return x * b


res = toy_example(torch.randn(10), torch.randn(10))
print(res.shape)


"""
notice:

POP_JUMP_IF_FALSE
__resume_at_
"""
