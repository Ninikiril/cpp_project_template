add_executable(testlib_name testlib_name.cpp)

find_package(Catch2 3 REQUIRED)

target_compile_features(testlib_name PRIVATE cxx_std_17)

target_link_libraries(testlib_name PRIVATE lib_name Catch2::Catch2WithMain)

add_test(NAME testlib_nametest COMMAND testlib_name)
