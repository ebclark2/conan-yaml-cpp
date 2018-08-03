project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_check_compiler()
#conan_output_dirs_setup()
conan_set_find_library_paths()
message(STATUS "Conan: Using cmake targets configuration")
conan_define_targets()
conan_set_rpath()
conan_set_vs_runtime()
conan_set_libcxx()
conan_set_find_paths()

add_executable(example example.cpp)
target_link_libraries(example CONAN_PKG::yaml-cpp)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
