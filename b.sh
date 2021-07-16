# clone repo && select branch

# get submodule
git submodule init
git submodule sync --recursive
git submodule update --init --recursive

# cmake build in vscode

# build torch_python

# DEBUG=1 LD_LIBRARY_PATH=${PWD}/build/lib python setup.py develop
DEBUG=1 LD_LIBRARY_PATH=/Users/allen/gglin001/pytorch/build/lib python setup.py develop

# debug python & cpp
