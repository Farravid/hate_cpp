cmake_minimum_required(VERSION 3.15)
project (Hate_cpp_benchmark CXX)

set(CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/../build")

find_package(benchmark REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE benchmark::benchmark_main)