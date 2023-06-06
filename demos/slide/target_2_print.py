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
    # print("gm.forward.__code__:")
    # [print(x) for x in dis.get_instructions(gm.forward.__code__)]
    return gm.forward


def add_raw(a, b):
    c = a + b
    return c


@dynamo.optimize(my_compiler)
def add(a, b):
    c = a * b
    print('start_forward')
    d = c + c
    return d


# [print(x) for x in list(dis.get_instructions(add_raw.__code__))]
# [print(x) for x in list(dis.get_instructions(add.__code__))]


x = torch.randn(10, requires_grad=False)
y = torch.randn(10, requires_grad=False)

z = add(x, y)
print(f"res: {z}")

"""
注意 log 中的 __resume_at_
"""
