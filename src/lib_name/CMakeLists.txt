set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/lib_name/lib_name.hpp")

add_library(lib_name lib_name.cpp ${HEADER_LIST})
install(TARGETS lib_name ARCHIVE DESTINATION lib COMPONENT libraries)
install(FILES ${HEADER_LIST} DESTINATION include COMPONENT headers)

target_include_directories(lib_name PUBLIC ../../include)

target_compile_features(lib_name PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
