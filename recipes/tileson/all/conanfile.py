from conan import ConanFile
from conan.tools import files


class pkgRecipe(ConanFile):
    name = "tileson"
    package_type = "header-library"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        files.get(self, "https://github.com/SSBMTonberry/tileson/archive/refs/tags/v1.4.0.zip", strip_root=True)

    def package(self):
        files.copy(self, "include/*.h*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
