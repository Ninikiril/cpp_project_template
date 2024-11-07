set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/test_lib/lib.hpp")

add_library(test_library lib.cpp ${HEADER_LIST})

target_include_directories(test_library PUBLIC ../include)

target_compile_features(test_library PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
