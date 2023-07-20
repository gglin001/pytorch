from typing import List
import torch
import torch._dynamo as dynamo
import torch.fx
import logging
import torch._dynamo
import dis

torch._logging.set_logs(dynamo=logging.DEBUG)
torch._logging.set_logs(all=logging.DEBUG)
# torch._dynamo.config.suppress_errors = True


def func(a, b):
    c = a + b
    return c


x = torch.randn(2, requires_grad=False)
y = torch.randn(2, requires_grad=False)

model = torch.compile(func, backend="onnxrt")

with torch.no_grad():
    inputs = [x, y]
    out = model(*inputs)
