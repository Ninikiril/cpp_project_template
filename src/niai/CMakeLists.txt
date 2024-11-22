set(HEADER_LIST "${PROJECT_SOURCE_DIR}/include/niai/niai.h")

add_library(niai niai.cpp ${HEADER_LIST})
install(TARGETS niai ARCHIVE DESTINATION lib COMPONENT niai_libs)
install(FILES ${HEADER_LIST} DESTINATION include COMPONENT niai_headers)

target_include_directories(niai PUBLIC ${PROJECT_SOURCE_DIR}/include)

target_compile_features(niai PUBLIC cxx_std_11)

source_group(
  TREE "${PROJECT_SOURCE_DIR}/include"
  PREFIX "Header Files"
  FILES ${HEADER_LIST})
