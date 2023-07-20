---
marp: true
---

# Introduction to TorchDynamo

Allen Guo
Jul 20 2023

---

# TOC

- torchdynamo
- PEP 523
- torch.fx
- Bytecode transform in torchdynamo
- Guard
- Backend

---

# torchdynamo

all starts from:

![width:700px](./imgs/TorchDynamo.png)

<!-- https://pytorch.org/docs/stable/dynamo/index.html -->

---

# PEP 523

> This PEP proposes to expand CPython’s C API to allow for the specification of a per-interpreter function pointer to handle the evaluation of frames

https://peps.python.org/pep-0523/

---

# torch.fx

- Python-based IR
- Support Python code generation

ref:

- https://pytorch.org/docs/main/fx.html
- https://arxiv.org/abs/2112.08429

---

# Bytecode transform in torchdynamo

a simple example

- target_0_add.py

---

# Bytecode transform in torchdynamo

more complex examples

- target_1_add_func.py
- target_2_print.py
- target_3_if.py
- target_4_module.py

- ...(Python & torch is very flexible)

---

# Guard

Speed up bytecode interpretation through caching
(wont be covered in this talk)

- https://github.com/pytorch/pytorch/blob/main/docs/source/compile/guards-overview.rst

- https://github.com/pytorch/pytorch/blob/main/docs/source/compile/deep-dive.rst

---

# Backend

- https://github.com/pytorch/pytorch/blob/main/docs/source/compile/custom-backends.rst

- traced Graph is wrapped into `torch.fx.GraphModule`, it is "normal" `torch.nn.Module`

## onnxrt

- check `torch/_dynamo/backends/onnxrt.py`
- onnxrt_add.py

---

# reference

all scripts are available at:

- https://github.com/gglin001/pytorch/tree/allen/thu_tea_230720/slide

more about torch(2.0+):

- https://pytorch.org/get-started/pytorch-2.0
- https://pytorch.org/docs/main/compile/index.html

pytorch dev-discuss(compiler)

- https://dev-discuss.pytorch.org/c/compiler/5

---

## Bakeup

- TODO
