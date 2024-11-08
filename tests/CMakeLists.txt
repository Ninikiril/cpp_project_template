add_executable(testlib testlib.cpp)

target_compile_features(testlib PRIVATE cxx_std_17)

target_link_libraries(testlib PRIVATE lib)

add_test(NAME testlibtest COMMAND testlib)
