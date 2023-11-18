pip install -r requirements.txt

# shallow clone submodules
git submodule update --recursive --init --depth=1
# git submodule update --recursive --shallow-submodules

# mamba install glog=0.4.0

# build with cmake in vscode

# pip install -e .
python setup.py develop

# DEBUG=1 \
#   LD_LIBRARY_PATH=$(pwd)/build/lib \
#   python \
#   setup.py \
#   develop
