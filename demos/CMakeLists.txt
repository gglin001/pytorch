cmake_minimum_required(VERSION 3.5 FATAL_ERROR)
project(demos)

set(CMAKE_CXX_STANDARD 14)

# add_executable(demo demo.cpp)
# # target_include_directories(demo PRIVATE ${TORCH_INCLUDE_DIRS})
# # target_include_directories(demo PRIVATE ${ATen_CPU_INCLUDE})
# target_link_libraries(demo PRIVATE torch)
# set_property(TARGET demo PROPERTY CXX_STANDARD 14)

add_executable(mnist mnist.cpp)
target_link_libraries(mnist PRIVATE torch)

# add_executable(demo2 demo2.cpp)
# target_link_libraries(demo2 PRIVATE torch)

# add_executable(demo3 demo3.cpp)
# target_link_libraries(demo3 PRIVATE torch)
