from conans import ConanFile, CMake, tools


class YamlcppConan(ConanFile):
    name = "yaml-cpp"
    version = "master"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Yamlcpp here>"
    build_requires = "cmake_installer/1.0@conan/stable"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=False"
    generators = "cmake"
    exports_sources = "yaml-cpp/*"

    def build(self):
        cmake = CMake(self)
        if self.options.fPIC:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE:BOOL"] = "ON"
        cmake.configure(source_dir=self.source_folder + "/yaml-cpp")
        cmake.build()
        cmake.install();

    def package_info(self):
        if self.settings.compiler != "Visual Studio":
            self.cpp_info.libs = ["yaml-cpp"]
        else:
            self.cpp_info.libs = ["libyaml-cppmd"]
