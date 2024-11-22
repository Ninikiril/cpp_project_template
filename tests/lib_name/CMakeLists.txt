add_executable(test_lib_name test_lib_name.cpp)

find_package(Catch2 3 REQUIRED)

target_compile_features(test_lib_name PRIVATE cxx_std_17)

target_link_libraries(test_lib_name PRIVATE lib_name Catch2::Catch2WithMain)

add_test(NAME test_lib_nametest COMMAND test_lib_name)
