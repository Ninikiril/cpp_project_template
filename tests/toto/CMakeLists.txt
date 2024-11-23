add_executable(test_toto test_toto.cpp)

find_package(Catch2 3 REQUIRED)

target_compile_features(test_toto PRIVATE cxx_std_17)

target_link_libraries(test_toto PRIVATE toto Catch2::Catch2WithMain)

add_test(NAME test_tototest COMMAND test_toto)
