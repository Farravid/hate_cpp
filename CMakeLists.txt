cmake_minimum_required(VERSION 3.15)
project(Hate_cpp CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 23)

find_package(ZLIB REQUIRED)
find_package(uwebsockets REQUIRED)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE ZLIB::ZLIB uwebsockets::uwebsockets)