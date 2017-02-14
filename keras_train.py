#!/usr/bin/python -u

import numpy as np
import os, sys, random
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

np.random.seed(1337)
n_rows, n_cols, n_ch  = 100, 100, 1
n_classes = 2

# ========= Model ========
'''
Neural Net layers definitions
'''

def GetModel():
	model = Sequential()
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

	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	return model
# ========================



def ShowImage(img):
	'''
		Since incoming image is normalized to 0-1 (float) range, 
		multiply it with 255 and convert to uint8 for display purposes
	'''
	img = np.array(img * 255, dtype='uint8').reshape(n_rows, n_cols, n_ch)
	cv2.imshow("Image", img)
	return cv2.waitKey(0)

def GetSample():
	'''
		Generate random class:
			0 = circle
			1 = square

		Draw circle / square of random size.
		Normalize output image by dividing by 255. Convert image to float32
	'''
	cls = random.randint(0, n_classes-1)
	img = np.zeros((n_rows, n_cols, n_ch), dtype='uint8')

	if cls == 0:
		cv2.circle(img, (n_cols/2, n_rows/2), random.randint(10, n_cols/2 - 10), (255), -1)
	elif cls == 1:
		side = random.randint(10, n_cols/2 - 10)
		cv2.rectangle(img, (n_cols/2 - side, n_cols/2 - side), (n_cols/2 + side, n_cols/2 + side), (255), -1)

	channels = cv2.split(img)
	out_image = np.array(channels, dtype='float32') / 255.

	return cls, out_image

def GetBatch(batch_size):
	'''
		Return an array of multiple samples (labels, images)
	'''
	batch_labels, batch_images = [], []

	for i in range(0, batch_size):
		cls, image = GetSample()
		batch_images.append(image)
		batch_labels.append(cls)

	return np.array(batch_labels).reshape(batch_size, 1), np.array(batch_images)


if __name__ == '__main__':


	model = GetModel()

	n_iter = 201
	batch_size = 64
	test_interval = 20
	test_size = 100

	'''
	visualization setup
	'''
	vis_dictionary = {0:"circle",1:"square"}
	if len(sys.argv) == 2:
		visualize = True 
		test_size = 10
	else:
		visualize = False

	

	for it in range(n_iter):
		print '\rIteration:', it,

		label_train, imgs_train = GetBatch(batch_size)
		imgs_train = imgs_train.reshape(batch_size, n_rows, n_cols, 1)
		label_train = np_utils.to_categorical(label_train, n_classes)

		model.train_on_batch(imgs_train, label_train)


		if it % test_interval == 0:
		
			print '\nTesting...\n',
			labels, imgs = GetBatch(test_size)
			imgs_test = imgs.reshape(test_size, n_rows, n_cols, 1)
			labels_test = np_utils.to_categorical(labels, n_classes)

			if visualize:
				'''
				 To visualize we will let the net predict single images 
				'''
				score = model.predict_on_batch(imgs_test)

				counter = 0
				for i,l in zip(imgs,labels):

					print("prediction vs. actual: \t {} {}".format(vis_dictionary[score[counter].argmax()],vis_dictionary[l[0]]))
					ShowImage(i)
					counter+= 1
			else:
				'''
					If we are not visualizing we are simply testing our net on a batch of data
				'''
				score = model.test_on_batch(imgs_test, labels_test)
				print  "Accuracy:{0:.0f}%\n".format( score[1]*100)

			














