"""Create the structure of a new app in the project."""
import os

from typing import List

def create_app_structure(app_name: str, libs: list[str]) -> None:
    """Create the structure of a new app in the project."""
    # Define the directory structure
    _dir = f"apps/{app_name}"
    os.makedirs(_dir, exist_ok=True)
    # Create base file
    base_files = f"apps/{app_name}/{app_name}.cpp"
    with open(base_files, 'w') as file:
        file.write("// Source file for the app\n")
    # CMakelists.txt
    cmake_content = f"""add_executable({app_name} {app_name}.cpp)
install(TARGETS {app_name} RUNTIME DESTINATION bin COMPONENT applications)

target_compile_features({app_name} PRIVATE cxx_std_17)

target_link_libraries({app_name} PRIVATE {' '.join(libs)})
"""
    cmake_file = f"apps/{app_name}/CMakeLists.txt"
    with open(cmake_file, 'w') as file:
        file.write(cmake_content)
    # Add the app to the main CMakeLists.txt
    with open("CMakeLists.txt", 'a') as file:
        file.write(f"add_subdirectory(apps/{app_name})\n")

if __name__ == "__main__":
    app_name = input("Enter the name of the app: ")
    number_of_libs = int(input("Enter the number of libraries to add to the app: "))
    libs = []
    for i in range(number_of_libs):
        lib_name = input(f"Enter the name of library {i+1}: ")
        libs.append(lib_name)
    create_app_structure(app_name, libs)
