# Conan Local Recipes Index Repository

## Prerequisites

* [Conan 2](https://docs.conan.io/2/)

## Usage
### Add local repo
```bash
  conan remote add localrepo . --allowed-packages="gl3w/*,openal/*,tileson/*"
```

### Install packages
```bash
conan install --requires=gl3w/1.0 -r=localrepo --build=missing
conan install --requires=tileson/1.4.0 -r=localrepo --build=missing
conan install --requires=openal/1.24.3 -r=localrepo --build=missing
```