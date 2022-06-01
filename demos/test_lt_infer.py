import torch
import torch.nn as nn
import torch._lazy
import torch._lazy.ts_backend
import torch._lazy.metrics

torch._lazy.ts_backend.init()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x, y):
        z = torch.mul(x, y)
        return z


device = 'lazy'

a = torch.rand(size=(2, 2), dtype=torch.float32)
b = torch.rand(size=(2, 2), dtype=torch.float32)
a = a.to(device)
b = b.to(device)
model = Net().to(device)

res = model(a, b)

# print('\n\n------------------ start print()')
# print(res)
# print('------------------ fin print()')

print('\n\n------------------ start mark_step()')
torch._lazy.mark_step()
print('------------------ fin mark_step()')
