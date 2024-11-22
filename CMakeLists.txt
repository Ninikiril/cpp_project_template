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

# packaging
include(CPack)

# subdirectories for lib_name
add_subdirectory(src/lib_name)
add_subdirectory(tests/lib_name)

# subdirectories for app_name
add_subdirectory(apps/app_name)

# components for app_name
cpack_add_component(app_name_apps)
cpack_add_component(lib_name_libs)
cpack_add_component(lib_name_headers)
