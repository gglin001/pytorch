from typing import List
import torch
import torch._dynamo as dynamo
import torch.fx
import logging
import torch._dynamo
import dis


torch._logging.set_logs(dynamo=logging.DEBUG)
torch._logging.set_logs(all=logging.DEBUG)


def my_compiler(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
    print("my_compiler() called with FX graph:")
    # gm.graph.print_tabular()
    return gm.forward


@dynamo.optimize(my_compiler)
def func(a, b):
    c = a * b
    print('print_here')
    d = c + c
    return d


x = torch.randn(10, requires_grad=False)
y = torch.randn(10, requires_grad=False)
z = func(x, y)
print(f"res: {z}")

"""
注意 log 中的

Unsupported
__resume_at_
JUMP_ABSOLUTE
"""
