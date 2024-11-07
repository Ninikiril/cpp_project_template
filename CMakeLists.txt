cmake_minimum_required(VERSION 3.15...3.30)

project(
  cpp_project_name
  VERSION 0.1
  DESCRIPTION "project_description"
  LANGUAGES CXX)

# Optionally set things like CMAKE_CXX_STANDARD, CMAKE_POSITION_INDEPENDENT_CODE here
set(CMAKE_CXX_EXTENSIONS OFF)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
include(CTest)

find_package(Doxygen)
if(Doxygen_FOUND)
  add_subdirectory(docs)
else()
  message(STATUS "Doxygen not found, not building docs")
endif()

add_subdirectory(src)

add_subdirectory(apps)

add_subdirectory(tests)
