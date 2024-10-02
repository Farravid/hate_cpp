cmake_minimum_required(VERSION 3.15)
project(Hate_cpp_test CXX)

include(../cmake/CPM.cmake)

set(CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/../build")
find_package(GTest REQUIRED)


message(STATUS ${CMAKE_CURRENT_LIST_DIR}/..)
CPMAddPackage(NAME Hate_cpp SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/..)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE gtest::gtest Hate_cpp)