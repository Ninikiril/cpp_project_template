set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/toto/toto.h")

add_library(toto toto.cpp ${HEADER_LIST})
install(TARGETS toto ARCHIVE DESTINATION lib COMPONENT toto_libs)
install(FILES ${HEADER_LIST} DESTINATION include COMPONENT toto_headers)

target_include_directories(toto PUBLIC ${PROJECT_SOURCE_DIR}/include)

target_compile_features(toto PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
