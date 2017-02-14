# Basic introduction to Deep Leanring with Keras

Get a neural net trained in 3 steps!


## Step 1 Installation

* if you do not have pip : `sudo easy_install pip`

* install keras and tensor flow :  ` pip install tensorflow keras`

* for visualization : `pip install opencv-python` 
 
* to silence the annoying, useless warnings : `export TF_CPP_MIN_LOG_LEVEL=1`


## Step 2 Train

* `./keras_train.py` 

* for visualization:  `./keras_train.py 1 ` (press on any key for next image)


## Step 3 Understand

**Big picture**:  we train, then test our neural net. **The goal**: a net which classifies with an accuracy of 100%

### Training 

Create our data :
```python
if cls == 0:
		cv2.circle(img, (n_cols/2, n_rows/2), random.randint(10, n_cols/2 - 10), (255), -1)
elif cls == 1:
		side = random.randint(10, n_cols/2 - 10)
		cv2.rectangle(img, (n_cols/2 - side, n_cols/2 - side), (n_cols/2 + side, n_cols/2 + side), (255), -1)
```
Train our network with this data:

```python
model.train_on_batch(imgs_train, label_train)
```
### Testing

Every couple iterations test our net:

```python
score = model.test_on_batch(imgs_test, labels_test)
print  "Accuracy:{0:.0f}%\n".format( score[1]*100)
```

### The Net 

Here we initialize our neural net :

```
model = Sequential()
```

Then we just `.add` the layers we want to define our neural net architecture.

```
	model.add(Convolution2D(16, 5, 5, border_mode='valid', input_shape=(n_rows, n_cols, 1)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Convolution2D(32, 5, 5))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Flatten())
	model.add(Dense(128))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(n_classes))
	model.add(Activation('softmax'))
```

A basic description of the layers:

* Convolution2d → extracting local image information 
* Activation → evaluate information relevance (in our case is it a white part of the image?)
* MaxPooling2D → image compression
* Dropout → avoiding bias
* Flatten → reformat  
* Dense → evaluate global image information (fully connected layer)
* Softmax → 'normalize' information


And last but not least this defines how our network should learn, which we use when training: 

```
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```



[backprop](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)





 
 
