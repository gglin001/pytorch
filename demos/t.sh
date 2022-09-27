pip install -r requirements.txt

# mamba install glog=0.4.0

# build with cmake in vscode

DEBUG=1 \
LD_LIBRARY_PATH=`pwd`/build/lib \
python \
setup.py \
develop
