#!/bash/bash

#
# General environment setup for python & opencv development 
#

# update apt-get libraries
sudo apt-get -y update
sudo apt-get -y upgrade

# install general tools
sudo apt-get -y install vim tmux unzip pkg-config
sudo apt-get -y install python3 python3-pip

# install developer tools
sudo apt-get -y install build-essential cmake 

# install OpenCV dependency libraries
sudo apt-get -y install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libatlas-base-dev gfortran
#Notes: needs to install below python library for opencv to find python
#       & link opencv to python
sudo apt-get -y install python3-dev python3-numpy

# download, build & install Opencv 4.1.0
mkdir ~/opencv
cd ~/opencv
wget -O opencv_4.1.0.zip https://github.com/opencv/opencv/archive/4.1.0.zip
wget -O opencv_contrib_4.1.0.zip https://github.com/opencv/opencv_contrib/archive/4.1.0.zip
unzip opencv_4.1.0.zip
unzip opencv_contrib_4.1.0.zip
cd opencv-4.1.0
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D WITH_CUDA=OFF \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules \
      -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

# installed libraries for PyImageSearch Gurus class 
# (not necessary for other purpose)
python3 -m pip install imutils

