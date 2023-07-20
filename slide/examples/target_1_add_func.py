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


def add(a, b):
    c = a + b
    return c


@dynamo.optimize(my_compiler)
def func(x, y):
    xx = x - x
    c = add(xx, y)
    return c


x = torch.randn(10, requires_grad=False)
y = torch.randn(10, requires_grad=False)
z = func(x, y)
print(f"res: {z}")


"""
注意 log 中
INLINING
"""
