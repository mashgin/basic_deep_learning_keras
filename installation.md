
### Installation for Ubuntu


* easy installation: pip → ` apt-get update && apt-get -y install python-pip`
    	
* visualization: opencv → ` sudo apt-get install libopencv-dev python-opencv`
	
	
* parsing: h5py → `sudo pip install h5py`

* deep learning library →  ` pip install tensorflow keras`
 
* silence annoying, useless warnings → `export TF_CPP_MIN_LOG_LEVEL=2`



### Installation for mac

* easy installation → install [brew](https://brew.sh)

* python → `brew install python`

* use the python we just installed → `hash -r python`

* deep learning library → `sudo pip install tensorflow keras`
	* if you run into this [problem](https://github.com/tensorflow/tensorflow/issues/6331) you can try workarounds mentioned in the link. The one that wokred for me was:
		* [disabaling](https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/) the Systems Integrity Protection on mac allowing the sudo user to more install rights. 
		* Running ` sudo pip install tensorflow keras` again 
		* After installing tensorflow and keras you can then [enable](https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/) the Systems Integrity Protection again. 

* parsing: h5py → `sudo pip install h5py`

* visualization: opencv →

	* `brew tap homebrew/science`

	* `brew install opencv`

* silence annoying, useless warnings → `export TF_CPP_MIN_LOG_LEVEL=1`


