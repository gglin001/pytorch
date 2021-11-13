#include <torch/torch.h>

#include <cstddef>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include "ATen/Functions.h"
#include "ATen/core/TensorBody.h"

const auto pp = [](torch::Tensor& x) {
  std::cout << "\n\ntensor:"
            << "\n";
  at::print(std::cout, x, 99);
};

auto main() -> int {
  torch::manual_seed(1);
  torch::Device device(torch::kCPU);

  auto x = torch::randn({2, 2}, torch::requires_grad());
  pp(x);

  // auto y = x + 2;
  // pp(y);
  // std::cout << y.grad_fn()->name() << std::endl;
  // auto z = y * y * 3;
  // auto out = z.mean();
  // std::cout << z << std::endl;
  // std::cout << z.grad_fn()->name() << std::endl;
  // std::cout << out << std::endl;
  // std::cout << out.grad_fn()->name() << std::endl;

  auto out = x.mean();
  std::cout << out.grad_fn()->name() << std::endl;

  out.backward();
  std::cout << x.grad() << std::endl;

  std::cout << "\nend"
            << "\n";
}
