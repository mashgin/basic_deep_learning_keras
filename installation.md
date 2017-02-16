
# Ubuntu


* easy installation: pip → ` apt-get update && apt-get -y install python-pip libopencv-dev python-opencv`

* deep learning library →  `sudo  pip install tensorflow keras h5py`
 
* silence warnings → `export TF_CPP_MIN_LOG_LEVEL=2`

* `git clone https://github.com/mashgin/basic_deep_learning_keras.git` 


# Mac

* remove brew → `rm -rf /usr/local/*`

* clean install brew → install [brew](https://brew.sh)

* python and opencv → `brew tap homebrew/science` and `brew install python opencv `

* use the python we just installed → `hash -r python`

* silence warnings → `export TF_CPP_MIN_LOG_LEVEL=2`

* `git clone https://github.com/mashgin/basic_deep_learning_keras.git` 


# Windows

* download and install [anaconda](https://www.continuum.io/downloads)

* `pip install keras opencv-python`

* change backend for keras to theano

	* open ` c:\Users\<username>\.keras\keras.json`

	* change `tensorflow` to `theano`
	

* install [git](https://git-scm.com/download/win)

* `git clone https://github.com/mashgin/basic_deep_learning_keras.git` 



