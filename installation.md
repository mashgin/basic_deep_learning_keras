
### Installation for Ubuntu


* for easy installation: pip -> ` apt-get update && apt-get -y install python-pip`
    
	
* for visualization: opencv -> ` sudo apt-get install libopencv-dev python-opencv`
	
	
* for saving the network: h5py -> `sudo pip install h5py`

* install keras and tensor flow ->  ` pip install tensorflow keras`
 
* to silence the annoying, useless warnings: `export TF_CPP_MIN_LOG_LEVEL=1`



### Installation for mac

* for easy installation: pip -> `sudo easy_install pip`



* install keras and tensor flow ->  ` sudo pip install tensorflow keras`

	* if you run into this [problem](https://github.com/tensorflow/tensorflow/issues/6331) you can try workarounds mentioned in the link. The one that wokred for me was:
		* [disabaling](https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/) the Systems Integrity Protection on mac allowing the sudo user to more install rights. 
		* Running ` sudo pip install tensorflow keras` again 
		* After installing tensorflow and keras you can then [enable](https://www.igeeksblog.com/how-to-disable-system-integrity-protection-on-mac/) the Systems Integrity Protection again. 
 
* for visualization: opencv -> `pip install opencv-python`
 
* to silence the annoying, useless warnings: `export TF_CPP_MIN_LOG_LEVEL=1`




