import os
from subprocess import call

from conan import ConanFile
from conan.tools import files
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class pkgRecipe(ConanFile):
    name = "gl3w"
    #version = "1.0"
    package_type = "library"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def source(self):
        files.download(self,
                       "https://raw.githubusercontent.com/skaslev/gl3w/4f1d558410b0938840dc3db98e741d71f382ba22/gl3w_gen.py",
                       "gl3w_gen.py")
        opts = "--ext"
        call(["python", os.path.join(self.source_folder, "gl3w_gen.py"), opts])

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        files.copy(self, "include/*.h*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.libs = ["gl3w"]
