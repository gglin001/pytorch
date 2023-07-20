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


def func1(a0, b0):
    print("func1")
    c = a0 + b0
    return c


def func0(a, b):
    c = func1(a, b)
    return c


@dynamo.optimize(my_compiler)
def func(a, b):
    d = func0(a, b)
    return d


in_a = torch.randn(10, requires_grad=False)
in_b = torch.randn(10, requires_grad=False)
res = func(in_a, in_b)

"""
4 times of

MODIFIED BYTECODE
"""
