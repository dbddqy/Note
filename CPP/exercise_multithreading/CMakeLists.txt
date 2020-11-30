project(exercise_multithreading)
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++11 -pthread")
#set(CMAKE_CXX_FLAGS "-std=c++14 -O3")
cmake_minimum_required(VERSION 3.15)

add_executable(join_detach join_detach.cpp)
add_executable(pass_argument pass_argument.cpp)
add_executable(lock lock.cpp)