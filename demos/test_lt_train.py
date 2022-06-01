import torch
import torch.nn as nn
import torch.optim as optim
import torch._lazy
import torch._lazy.ts_backend
import torch._lazy.metrics

torch._lazy.ts_backend.init()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.w = torch.nn.Parameter(torch.randn(2, 2))

    def forward(self, x):
        x = torch.mul(x, self.w)
        return x


device = 'lazy'

a = torch.rand(size=(2, 2), dtype=torch.float32)
a = a.to(device)
model = Net().to(device)
optimizer = optim.Adadelta(model.parameters(), lr=0.01)

for epoch in range(0, 1):
    model.train()
    output = model(a)
    loss = torch.mean(output)
    loss.backward()
    optimizer.step()

    # print('\n\n------------------ start print()')
    # print(loss)
    # print('------------------ fin print()')

    print('\n\n------------------ start mark_step()')
    torch._lazy.mark_step()
    print('------------------ fin mark_step()')
