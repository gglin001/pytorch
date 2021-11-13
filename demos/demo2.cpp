#include <torch/torch.h>

#include <cstddef>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include "ATen/Functions.h"
#include "ATen/core/TensorBody.h"
#include "glog/logging.h"
#include "torch/serialize.h"
#include "torch/serialize/input-archive.h"

struct NetImpl : torch::nn::Module {
  NetImpl() : conv1(torch::nn::Conv2dOptions(3, 3, 1).bias(false)) {
    register_module("conv1", conv1);
  }

  torch::Tensor forward(torch::Tensor x) {
    x = conv1->forward(x);
    return x;
  }
  torch::nn::Conv2d conv1;
};

TORCH_MODULE(Net);

const auto pp = [](torch::Tensor& x) {
  std::cout << "\n\ntensor:"
            << "\n";
  at::print(std::cout, x, 99);
};

auto main() -> int {
  torch::manual_seed(1);
  torch::Device device(torch::kCPU);

  Net model;
  model->to(device);

  // torch::optim::SGD optimizer(
  //     model->parameters(), torch::optim::SGDOptions(0.01).momentum(0.5));

  // auto options = at::TensorOptions().requires_grad(true);
  auto x = torch::ones({1, 3, 2, 2}, torch::requires_grad());
  // auto x = torch::randn({1, 3, 2, 2}, options);
  auto y = model->forward(x);
  pp(x);
  pp(y);
  // at::Tensor loss = torch::l1_loss(y, y);

  // optimizer.zero_grad();

  y.backward();
  // auto y_grad = y.grad();
  // pp(y_grad);

  // auto y_grad_fn = y.grad_fn();

  std::cout << "\nend"
            << "\n";
}
