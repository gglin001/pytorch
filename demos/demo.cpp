#include <torch/torch.h>
#include <iostream>

void func1() {
  torch::Tensor tensor = torch::rand({2, 3});
  std::cout << tensor << std::endl;
  std::cout << "1" << std::endl;
}

void func2() {

  std::cout << "1" << std::endl;
}

int main() {
  std::cout << "0" << std::endl;

  return 0;
}