add_executable(testlib testlib.cpp)

target_compile_features(testlib PRIVATE cxx_std_17)

target_link_libraries(testlib PRIVATE test_library)

add_test(NAME testlibtest COMMAND testlib)
