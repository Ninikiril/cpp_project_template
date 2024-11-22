""" Create the directory structure for a library """
import json
import os

def add_lib_to_project(lib_name: str) -> None:
    """ Create the directory structure for a library """
    # Define the directory structure
    dirs = [
        f"src/{lib_name}",
        f"include/{lib_name}",
        f"tests/{lib_name}"
    ]
    # Create directories
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

    # Create cpp, h, and test files
    with open(f"src/{lib_name}/{lib_name}.cpp", 'w') as file:
            file.write(f'#include "{lib_name}/{lib_name}.h"\n\n')
            file.write(f'namespace {lib_name}' + '{\n')
            file.write('bool functionNameF(const Real realV)\n')
            file.write('{\n')
            file.write('    return realV > 0.0f;\n')
            file.write('}\n')
            file.write('} '+f'// namespace {lib_name}\n')

    with open(f"include/{lib_name}/{lib_name}.h", 'w') as file:
        file.write('#pragma once\n\n')
        file.write(f'namespace {lib_name} ' + '{\n')
        file.write('/// @brief Example function\n')
        file.write('///\n')
        file.write('/// @details This function is an example of a function. It returns true if a is\n')
        file.write('/// greater than 0, false otherwise.\n')
        file.write('///\n')
        file.write('/// @param aV\n')
        file.write('/// @return true\n')
        file.write('/// @return false\n\n')
        file.write('using Real = float;\n\n')
        file.write('bool functionNameF(const Real realV);\n')
        file.write('} '+f'// namespace {lib_name}\n')

    with open(f"tests/{lib_name}/test_{lib_name}.cpp", 'w') as file:
        file.write('#include <catch2/catch_test_macros.hpp>\n')
        file.write(f'#include <{lib_name}/{lib_name}.h>\n\n')
        file.write(f'TEST_CASE("{lib_name}::functionName" )'+'{\n')
        file.write(f'    REQUIRE({lib_name}::functionNameF(1.0f));\n')
        file.write(f'    REQUIRE_FALSE({lib_name}::functionNameF(-1.0f));\n')
        file.write('}\n')

    # CMakelists.txt
    with open(f"src/{lib_name}/CMakeLists.txt", 'w') as file:
        file.write(f'set(HEADER_LIST "${{PROJECT_SOURCE_DIR}}/include/{lib_name}/{lib_name}.h")\n\n')
        file.write(f'add_library({lib_name} {lib_name}.cpp ${{HEADER_LIST}})\n')
        file.write(f'install(TARGETS {lib_name} ARCHIVE DESTINATION lib COMPONENT {lib_name}_libs)\n')
        file.write(f'install(FILES ${{HEADER_LIST}} DESTINATION include COMPONENT {lib_name}_headers)\n\n')
        file.write(f'target_include_directories({lib_name} PUBLIC ${{PROJECT_SOURCE_DIR}}/include)\n\n')
        file.write(f'target_compile_features({lib_name} PUBLIC cxx_std_11)\n\n')
        file.write('source_group(\n')
        file.write('  TREE "${PROJECT_SOURCE_DIR}/include"\n')
        file.write('  PREFIX "Header Files"\n')
        file.write('  FILES ${HEADER_LIST})\n')

    with open(f"tests/{lib_name}/CMakeLists.txt", 'w') as file:
        file.write(f'add_executable(test_{lib_name} test_{lib_name}.cpp)\n\n')
        file.write('find_package(Catch2 3 REQUIRED)\n\n')
        file.write(f'target_compile_features(test_{lib_name} PRIVATE cxx_std_17)\n\n')
        file.write(f'target_link_libraries(test_{lib_name} PRIVATE {lib_name} Catch2::Catch2WithMain)\n\n')
        file.write(f'add_test(NAME test_{lib_name}test COMMAND test_{lib_name})\n')

    print(f"Library structure for '{lib_name}' created successfully.")

    # Add the library to the main CMakeLists.txt
    with open("CMakeLists.txt", 'a') as file:
        file.write(f"\n# subdirectories for {lib_name}\n")
        file.write(f"add_subdirectory(src/{lib_name})\n")
        file.write(f"add_subdirectory(tests/{lib_name})\n")

    print(f"Library '{lib_name}' added to the project.")

def add_build_config_and_packaging(lib_name: str) -> None:
    """ Add the build configuration for the CMakeUserPresets.json file """
    # Add build presets for the new library
    build_presets = [
        {
            "name": f"{lib_name}-release-build",
            "inherits": "release-build",
            "targets": [
                lib_name,
                f"test_{lib_name}"
            ]
        },
        {
            "name": f"{lib_name}-debug-build",
            "inherits": "debug-build",
            "targets": [
                lib_name,
                f"test_{lib_name}"
            ]
        },
        {
            "name": f"{lib_name}-debinfo-build",
            "inherits": "debinfo-build",
            "targets": [
                lib_name,
                f"test_{lib_name}"
            ]
        }
    ]

    # Add package presets for the new library
    package_presets = [
        {
            "name": f"{lib_name}-package",
            "inherits": "default-package",
            "configurations": [
                f"{lib_name}-release-build"
            ]
        }
    ]

    # Read the existing CMakeUserPresets.json file
    with open("CMakeUserPresets.json", 'r') as file:
        cmake_presets = json.load(file)

    # Add the new build and package presets
    cmake_presets["buildPresets"].extend(build_presets)
    cmake_presets["packagePresets"].extend(package_presets)

    # Write the updated CMakeUserPresets.json file
    with open("CMakeUserPresets.json", 'w') as file:
        json.dump(cmake_presets, file, indent=4)

    print(f"Build configuration and packaging for '{lib_name}' added successfully.")

if __name__ == "__main__":
    lib_name = input("Enter the name of the library: ")
    add_lib_to_project(lib_name)
    add_build_config_and_packaging(lib_name)
