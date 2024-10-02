cmake_minimum_required(VERSION 3.15)
project (hate_cpp_benchmark CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(benchmark REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE benchmark::benchmark_main)