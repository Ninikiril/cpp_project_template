add_executable(testlib testlib.cpp)

find_package(Catch2 3 REQUIRED)

target_compile_features(testlib PRIVATE cxx_std_17)

target_link_libraries(testlib PRIVATE lib Catch2::Catch2WithMain)

add_test(NAME testlibtest COMMAND testlib)
