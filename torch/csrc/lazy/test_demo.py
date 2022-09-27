import torch
import torch.nn as nn
import torch._lazy
import torch._lazy.ts_backend
import torch._lazy.metrics
import numpy as np


torch._lazy.ts_backend.init()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 2, 3, 1, bias=False)
        # self.w = torch.nn.Parameter(torch.rand(1, 3, 5, 5))

    def forward(self, x):
        x = self.conv1(x)
        # x = x + self.w
        return x


device = 'lazy'
model = Net().to(device)
model.train()

data = np.random.uniform(low=-10, high=10, size=[1, 3, 5, 5]).astype(np.float32)
data = torch.from_numpy(data)

for idx in range(2):
    data = data.to(device)
    output = model(data)
    output.retain_grad()
    loss = torch.mean(output)
    loss.retain_grad()
    loss.backward()

    print('\n\n------------------ start mark_step()')
    torch._lazy.mark_step()
    print('------------------ fin mark_step()')

    # print(data.grad)
    # print(model.w.grad)
    # print(loss.grad)
    print(output.grad)
