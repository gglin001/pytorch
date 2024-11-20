################################################################################

micromamba create -n torch python=3.12

micromamba activate torch

################################################################################

# git submodule update --recursive --init --depth=1
git submodule update --init --depth=1
git submodule update --init --recursive --depth 1 third_party/kineto
git submodule update --init --recursive --depth 1 third_party/tensorpipe

# build with cmake
# install with cmake

# pip install -r requirements.txt

pip install --no-build-isolation -i -e . -vvv
# python setup.py develop

################################################################################

# git submodule update --recursive --init --depth=1
git submodule update --init --depth=1
git submodule update --init --recursive --depth 1 third_party/kineto
git submodule update --init --recursive --depth 1 third_party/tensorpipe

rm -rf build/CMakeCache.txt
rm -rf build/CMakeFiles

# cmake --preset osx -S. -Bbuild
cmake --preset osx_allen -S. -Bbuild

cmake --build build -t all
# cmake --build build -t torch

# for osx
micromamba install findutils

find build/lib/*.so -printf "%f\n" | xargs -d "\n" -I{} ln -s $PWD/build/lib/{} $PWD/torch/lib/{}
find build/lib/*.dylib -printf "%f\n" | xargs -d "\n" -I{} ln -s $PWD/build/lib/{} $PWD/torch/lib/{}
find build/lib/*.a -printf "%f\n" | xargs -d "\n" -I{} ln -s $PWD/build/lib/{} $PWD/torch/lib/{}
ln -s $PWD/build/functorch/functorch.so $PWD/functorch/functorch.so
ln -s $PWD/build/bin $PWD/torch/bin

################################################################################

cmake --build build --target help
cmake --build build --target help >_demos/cmake.target.log

################################################################################
