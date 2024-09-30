################################################################################

git submodule update --recursive --init --depth=1

# build with cmake
# install with cmake

# pip install -r requirements.txt

pip install -e .
# python setup.py develop

################################################################################

# cmake --preset osx -S. -Bbuild
cmake --preset osx_allen -S. -Bbuild

cmake --build build -t all

# for zsh
# micromamba install findutils

# find build/lib/*.so -printf "%f\n" | xargs -d "\n" -I{} ln -s $PWD/build/lib/{} $PWD/torch/lib/{}
# ln -s $PWD/build/functorch/functorch.so $PWD/functorch/functorch.so
find build/lib/*.dylib -printf "%f\n" | xargs -d "\n" -I{} ln -s $PWD/build/lib/{} $PWD/torch/lib/{}
ln -s $PWD/build/functorch/functorch.so $PWD/functorch/functorch.so

################################################################################
