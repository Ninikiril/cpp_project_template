# C++ Project Template

This repository provides a template for C++ projects using Visual Studio Code, Vcpkg, Doxygen, and Visual Studio Community 2022.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Vcpkg](https://github.com/microsoft/vcpkg)
- [Doxygen](http://www.doxygen.nl/)
- [Visual Studio Community 2022](https://visualstudio.microsoft.com/vs/community/)

## Getting Started

### Install VS Community

Download Visual Studio Installer and install Desktop development with C++ and don't forget to add windows11 SDK and unselect vcpkg management from VS

### Install vscode

Install vscode and add the following extensions:
    C/C++
    C/C++ extension pack
    Python

### Install Dependencies

Install doxygen

### Clone the Repository

```sh
git clone https://github.com/Ninikiril/cpp_project_template.git
```

### Clone the vcpkg Repository

```sh
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.bat
```
make sure path to vcpkg/ has no white space

## Configure, Build and Run

open cpp_template or repo created from it in vscode

### CMakePresets.json && CMakeUserPresets.json
Change vscode setting "Cmake: Use CMake Presets" to "always"
change depending on what your config is.

In CMakeUserPresets.json there must be a config named "default-config" for the scripts to work properly

```sh
    "name": "default-config",
        "inherits": "your_config",
        "environment": {
        ...
```

### scripts

you might want to change reset.py script to set presets json files to what they are right now

use lib_create to add lib, lib_config to config the workflow and lib_delete to delete lib
same for app

### Status bar

You should be now good to go !

In the status bar you should find cmake tools extension if not right click and and toggle show the extension (if you can't find it you'll have to add the extension to vscode).

### Run and Debug

On the left Bar you'll find run and debug or (Ctrl + Shift + D) to launch either the apps or the tests

## Doxygen

To generate the doxygen select the docs_build build and build. In out/build/default/docs/html/ you'll find index.html you can open it using any browser

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE V3. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Visual Studio Code](https://code.visualstudio.com/)
- [Vcpkg](https://github.com/microsoft/vcpkg)
- [Doxygen](http://www.doxygen.nl/)
- [Visual Studio Community 2022](https://visualstudio.microsoft.com/vs/community/)