cmake_minimum_required(VERSION 3.15)
project(Hate_cpp_standalone CXX)

include(../cmake/CPM.cmake)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/../build")

CPMAddPackage(NAME Hate_cpp SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/..)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE Hate_cpp)