# Your first deep neural network in less than 5 minutes

**Big picture**:  Train a neural net with the keras framework to classify images of circles and squares:

![c1](img_examples/circle.png) ![s1](img_examples/square3.png)  ![c2](img_examples/circ_1.png) ![s4](img_examples/square3.png) ![c3](img_examples/circle_2.png) ![s2](img_examples/square.png) ![s3](img_examples/square2.png)  


## Getting started

### 1. Install libraries

Go ahead and [install](https://github.com/mashgin/basic_deep_learning_keras/blob/master/installation.md) everything you need (works on Linux, Mac, and Windows).


### 2. Train

Run `python keras_train.py t`	to train your network. This might take a minute to finish.


### 3. Classify

Run `python keras_train.py c` to classify your images. Press `spacebar` to see the next image and press `q` to quit.

## Understanding

### Training 

Here we create our data using OpenCV: images of cirles and squares with random dimensions. [→](keras_train.py#L59-L63)

```python
if cls == 0:
		cv2.circle(img, (n_cols/2, n_rows/2), random.randint(10, n_cols/2 - 10), (255), -1)
elif cls == 1:
		side = random.randint(10, n_cols/2 - 10)
		cv2.rectangle(img, (n_cols/2 - side, n_cols/2 - side), (n_cols/2 + side, n_cols/2 + side), (255), -1)
```


Then we train our neural net with the created data. [→](keras_train.py#L111)

```python
model.train_on_batch(imgs_train, label_train)
```

### Testing

Every couple iterations we test our neural net and calculate it's accuracy up to this point. [→](keras_train.py#L129)

```python
score = model.test_on_batch(imgs_test, labels_test)
print  "Accuracy:{0:.0f}%\n".format( score[1]*100)
```

### The Net

Before we can train and classify we need to create our neural net. [→](keras_train.py#L25)

```python
model = Sequential()
```

Then we just `.add` the layers we want to have in our neural net. In other words, define our neural net architecture. [→](keras_train.py#L26)

```python
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

Here's just a short description of the layers used in this neural net:

* **Convolution2d** → extracting local image information 
* **Activation** → evaluate information relevance
* **MaxPooling2D** → image compression
* **Dropout** → avoiding bias
* **Flatten** → reformat  
* **Dense** → evaluate global image information (fully connected layer)

And last but not least, this defines how our neural net should learn, which we need for training: [→](keras_train.py#L41)

```python
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
```

If this tutorial got you excited about deep learning I recommend you start of looking into this [tutorial](http://adilmoujahid.com/posts/2016/06/introduction-deep-learning-python-caffe/) or the keras [documentation](https://keras.io). For those of you who have more time and would like a good read here's a good [book](http://neuralnetworksanddeeplearning.com/) . 

## About

This tutorial was created by [Amelie Frossle](https://github.com/ameliefroessl), an intern and now deep-learning-expert at Mashgin.

<img src="img_examples/mashgin.png" style="width: 200px;"/>

At [Mashgin](http://www.mashgin.com), we're creating better human experiences through visual automation. We work on lots of cool stuff in many industries. If you're interested, [drop us a line](mailto:contact@mashgin.com) or check out our [hiring page](http://mashgin.com/jobs.html).

### License

This tutorial is licensed under the MIT License. See [LICENSE](LICENSE) for more details. Feel free to clone, fork, or use any parts of the tutorial as long as they are attributed.

 
