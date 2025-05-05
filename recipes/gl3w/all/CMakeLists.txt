cmake_minimum_required(VERSION 3.15)
project(gl3w C)

add_library(${PROJECT_NAME} src/gl3w.c)
target_include_directories(${PROJECT_NAME}  PUBLIC include)

install(TARGETS ${PROJECT_NAME})
