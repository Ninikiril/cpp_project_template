cmake_minimum_required(VERSION 3.15...3.30)

project(
  cpp_project_name
  VERSION 0.1
  DESCRIPTION "project_description"
  LANGUAGES CXX)

set(CMAKE_CXX_EXTENSIONS OFF)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
include(CTest)

find_package(Doxygen)
if(Doxygen_FOUND)
  message(STATUS "Doxygen found, building docs")
  add_subdirectory(docs)
else()
  message(STATUS "Doxygen not found, not building docs")
endif()

add_subdirectory(src/lib)
add_subdirectory(tests/lib)

add_subdirectory(apps/app)
