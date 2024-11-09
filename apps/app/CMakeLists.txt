add_executable(app app.cpp)
target_compile_features(app PRIVATE cxx_std_17)

find_package(fmt CONFIG REQUIRED)

target_link_libraries(app PRIVATE lib fmt::fmt)
