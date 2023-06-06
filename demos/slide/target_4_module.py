# from test/dynamo/test_compile.py

from typing import List
import torch
import torch._dynamo as dynamo
import torch.fx
import logging
import torch._dynamo
import torch

torch._logging.set_logs(all=logging.DEBUG)
torch._logging.set_logs(dynamo=logging.DEBUG)

torch.random.manual_seed(0)


def my_compiler(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
    print("my_compiler() called with FX graph:")
    # gm.graph.print_tabular()
    return gm.forward


class ToyModel(torch.nn.Module):
    def __init__(self):
        super(ToyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        # print('start_forward')
        x -= 1.0  # sum ==1
        if x.sum() > 0.0:
            x += 1.0  # sum ==2
            return self.linear(x)
        x += 3.0
        return self.relu(self.linear(x))


model = ToyModel()
model = torch.compile(ToyModel(), backend=my_compiler)
x = torch.randn(10, 10)
res = model(x)
print(res.shape)
