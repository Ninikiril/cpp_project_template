cmake_minimum_required(VERSION 3.21)

project(
  cpp_project_name
  VERSION 0.1
  DESCRIPTION "project_description"
  LANGUAGES CUDA CXX)

# testing
include(CTest)

# generating docs with doxygen
find_package(Doxygen)
if(Doxygen_FOUND)
  message(STATUS "Doxygen found, building docs")
  add_subdirectory(docs)
else()
  message(STATUS "Doxygen not found, not building docs")
endif()

# subdirectories for the project libs
add_subdirectory(src/lib)
add_subdirectory(tests/lib)

# subdirectories for the project apps
add_subdirectory(apps/app)
