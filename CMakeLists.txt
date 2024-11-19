cmake_minimum_required(VERSION 3.21)

project(
  cpp_project_name
  VERSION 0.4.3
  DESCRIPTION "project_description"
  LANGUAGES CUDA CXX)

# testing
include(CTest)

# for SONAR LINT
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# generating docs with doxygen
find_package(Doxygen)
if(Doxygen_FOUND)
  message(STATUS "Doxygen found, building docs")
  add_subdirectory(docs)
else()
  message(STATUS "Doxygen not found, not building docs")
endif()

# subdirectories for the project libs
add_subdirectory(src/lib_name)
add_subdirectory(tests/lib_name)

# subdirectories for the project apps
add_subdirectory(apps/app_name)

# packaging
include(CPack)

# components for installation
cpack_add_component(applications)
cpack_add_component(libraries)
cpack_add_component(headers)
