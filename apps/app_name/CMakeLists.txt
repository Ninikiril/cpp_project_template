add_executable(app_name app_name.cpp)
install(TARGETS app_name RUNTIME DESTINATION bin COMPONENT applications)

target_compile_features(app_name PRIVATE cxx_std_17)

target_link_libraries(app_name PRIVATE lib_name)
