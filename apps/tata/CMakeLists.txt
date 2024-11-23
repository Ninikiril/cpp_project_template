add_executable(tata tata.cpp)
install(TARGETS tata RUNTIME DESTINATION bin COMPONENT tata_apps)

target_compile_features(tata PRIVATE cxx_std_17)

target_link_libraries(tata PRIVATE toto)
