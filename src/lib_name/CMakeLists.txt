set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/lib_name/lib_name.h")

add_library(lib_name lib_name.cpp ${HEADER_LIST})
install(TARGETS lib_name ARCHIVE DESTINATION lib COMPONENT lib_name_libs)
install(FILES ${HEADER_LIST} DESTINATION include COMPONENT lib_name_headers)

target_include_directories(lib_name PUBLIC ${PROJECT_SOURCE_DIR}/include)

target_compile_features(lib_name PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
