cmake_minimum_required(VERSION 3.21)

set(PROJECT_NAME "cpp_project_name")
set(PROJECT_DESCRIPTION "project_description")
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_VERSION_PATCH 0)
set(PROJECT_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}")
set(PROJECT_SOURCE_DIR "${CMAKE_SOURCE_DIR}")
set(PROJECT_BINARY_DIR "${CMAKE_BINARY_DIR}")
set(PROJECT_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}")
set(PROJECT_URL "https://github.com/Ninikiril/cpp_project_template")
set(PROJECT_AUTHOR "Nicolas Planard-Luong")
set(PROJECT_AUTHOR_EMAIL "nicolas.planard.luong@gmail.com")

project(
  ${PROJECT_NAME}
  VERSION ${PROJECT_VERSION}
  DESCRIPTION ${PROJECT_DESCRIPTION}
  LANGUAGES CUDA CXX)

# includes
include(CTest)

# for SONAR LINT
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# generating docs with doxygen
find_package(Doxygen)
if(Doxygen_FOUND)
  message(STATUS "Doxygen found, building docs")
  add_subdirectory(docs)
else()
  message(STATUS "Doxygen not found, not building docs")
endif()

set(PROJECT_LIBS "")
file(READ ${CMAKE_SOURCE_DIR}/json/project_data.json json_content)
string(JSON lib_count GET ${json_content} lib_count)
if(lib_count STREQUAL "-1")
  message(WARNING "No libraries found in json file")
else()
  foreach(lib_index RANGE ${lib_count})
    string(JSON lib_name GET ${json_content} libs ${lib_index})
    list(APPEND PROJECT_LIBS ${lib_name})
  endforeach()
endif()
string(JSON app_count GET ${json_content} app_count)
if(app_count STREQUAL "-1")
  message(WARNING "No apps found in json file")
else()
  foreach(app_index RANGE ${app_count})
    string(JSON app_name GET ${json_content} apps ${app_index} name)
    list(APPEND PROJECT_APPS ${app_name})
  endforeach()
endif()

foreach(lib ${PROJECT_LIBS})
  add_subdirectory(src/${lib})
  add_subdirectory(tests/${lib})
  install(TARGETS ${lib} ARCHIVE DESTINATION lib)
endforeach()
foreach(app ${PROJECT_APPS})
  add_subdirectory(apps/${app})
  install(TARGETS ${app} RUNTIME DESTINATION bin)
endforeach()

foreach(lib ${PROJECT_LIBS})
  file(GLOB_RECURSE lib_headers ${CMAKE_SOURCE_DIR}/include/${lib}/*.h)
  install(FILES ${lib_headers} DESTINATION include/${lib})
endforeach()

set(CPACK_GENERATOR "NSIS")
set(CPACK_PACKAGE_NAME ${PROJECT_NAME})
set(CPACK_PACKAGE_VENDOR ${PROJECT_AUTHOR})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY ${PROJECT_DESCRIPTION})
set(CPACK_PACKAGE_VERSION_MAJOR ${PROJECT_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${PROJECT_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${PROJECT_VERSION_PATCH})
set(CPACK_PACKAGE_VERSION ${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH})
set(CPACK_NSIS_INSTALL_ROOT "C:\\\\Program Files")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "${PROJECT_NAME}")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY ${PROJECT_NAME})
set(CPACK_IGNORE_FILES "")
set(CPACK_SOURCE_GENERATOR "TGZ")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}")
set(CPACK_SOURCE_IGNORE_FILES ${CPACK_IGNORE_FILES})
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/resources/nsis ${CMAKE_MODULE_PATH})
set(CPACK_NSIS_MODIFY_PATH OFF)
set(CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL ON)

INCLUDE(CPack)

configure_file(
  ${PROJECT_SOURCE_DIR}/resources/nsis/NSIS.definitions.nsh.in
  ${CMAKE_CURRENT_BINARY_DIR}/resources/nsis/NSIS.definitions.nsh
)