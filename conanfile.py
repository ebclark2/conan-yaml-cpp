from conans import ConanFile, CMake, tools


class YamlcppConan(ConanFile):
    name = "yaml-cpp"
    version = "master"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Yamlcpp here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/jbeder/yaml-cpp.git")
        self.run("cd yaml-cpp")

    def build(self):
        cmake = CMake(self)
        CMAKE_OPTIONS = ""
        if self.options.fPIC:
            CMAKE_OPTIONS += "-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON"
        self.run('cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON %s %s yaml-cpp' % (cmake.command_line, CMAKE_OPTIONS))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="yaml-cpp/include")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["yaml-cpp"]
