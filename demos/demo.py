import os  # isort: skip
import sys  # isort: skip

# torch_path = os.path.dirname(os.path.dirname(__file__))
torch_path = '/data/songlin/repos/pytorch/'
sys.path.insert(0, torch_path)
import torch  # isort: skip

torch.set_num_threads(1)
print(os.getpid())
print(torch.__file__)

a = torch.Tensor([-1, 2, -3])
b = torch.Tensor([-1, 2, -3])
# set breakpoint here and related c++ code
# c++ add breakpoint at `add_stub` in
# `aten/src/ATen/native/BinaryOps.cpp`
# for debuging kernel-dispatching process
c = torch.add(a, b)
print(c)
