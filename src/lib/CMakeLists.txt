set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/lib/lib.hpp")

add_library(lib lib.cpp ${HEADER_LIST})

target_include_directories(lib PUBLIC ../../include)

target_compile_features(lib PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
