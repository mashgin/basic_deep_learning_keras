# Ubuntu


Easy installation:

```sh
# Install pip and OpenCV
apt-get update && apt-get -y install python-pip libopencv-dev python-opencv

# Install the deep learning libraries
sudo pip install tensorflow keras h5py

# Silence irrelevant warnings
export TF_CPP_MIN_LOG_LEVEL=2

# Clone the tuturial repo
git clone https://github.com/mashgin/basic_deep_learning_keras.git
```

# Mac

First, make sure you have [Homebrew](https://brew.sh) installed. Then run the following:

```sh
# Install OpenCV & libraries
brew tap homebrew/science
brew install python opencv

# Use the Python we just installed
hash -r python

# Install the deep learning libraries
pip install tensorflow keras h5py

# Silence irrelevant warnings
export TF_CPP_MIN_LOG_LEVEL=2

# Clone the tuturial repo
git clone https://github.com/mashgin/basic_deep_learning_keras.git
```
If you run into [this problem](https://github.com/tensorflow/tensorflow/issues/6331) installing the deep learning libraries, you can try workarounds mentioned in the link. The one that worked for me was temporarily [disabaling the Systems Integrity Protection](https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/) giving the sudo user more install rights.

# Windows

* First download and install [Anaconda](https://www.continuum.io/downloads).

* In the Anaconda terminal, install OpenCV and Keras: `pip install keras opencv-python`

* Change backend for Keras to Theano

	* Open `c:\Users\<username>\.keras\keras.json`

	* Change `tensorflow` to `theano`
* Make sure [Git](https://git-scm.com/download/win) is installed.

* Clone the tuturial repo: `git clone https://github.com/mashgin/basic_deep_learning_keras.git`


