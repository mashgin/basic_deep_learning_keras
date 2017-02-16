#!/usr/bin/python -u

import numpy as np
import os, sys, random
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
from keras.models import load_model


np.random.seed(1337)
n_rows, n_cols, n_ch  = 100, 100, 1
n_classes = 2

# ========= Model ========

def GetModel():
	
	'''
		Defining Neural Net layers 
	'''
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


def train():

	'''
		Train the neural net and test the accuracy every couple iterations
	'''

	model = GetModel()

	n_iter = 61
	batch_size = 64
	test_interval = 20
	test_size = 100

	for it in range(n_iter):
		print '\rIteration:', it,

		'''
			Get a batch of data (batch_size many images with corresponding labels)
		'''
		label_train, imgs_train = GetBatch(batch_size)
		imgs_train = imgs_train.reshape(batch_size, n_rows, n_cols, 1)
		label_train = np_utils.to_categorical(label_train, n_classes)

		'''
			train the neureal net with this batch of data
		'''
		model.train_on_batch(imgs_train, label_train)


		if it % test_interval == 0:
		
			print '\nTesting...\n',
			
			'''
				Get a batch of data to test on 
			'''
			
			labels, imgs = GetBatch(test_size)
			imgs_test = imgs.reshape(test_size, n_rows, n_cols, 1)
			labels_test = np_utils.to_categorical(labels, n_classes)

			'''
				evaluate how well the neural net alraedy classifies this batch of data
			'''
			score = model.test_on_batch(imgs_test, labels_test)
			print  "Accuracy:{0:.0f}%\n".format( score[1]*100)

	'''
		Save to file for later use
	'''
	model.save('weights.h5')


def classify():

	'''
		Load the trained network
	'''
	model = load_model('weights.h5')

	'''
		For fancy output
	'''
	vis_dictionary = {0:"circle",1:"square"}

	'''
		Get an image, let the network  predict what it is, 
		output the image and the prediciton
	'''

	while(True):
		
		'''
			Get data (images )
		'''
		label, img = GetBatch(1)
		img_test = img.reshape(1, n_rows, n_cols, 1)
		label_test = np_utils.to_categorical(label, n_classes)

		'''
			Predict whats in the image with our neural net
		'''
		score = model.predict_on_batch(img_test)

		'''
			create fancy window pop up 
		'''
		img2 = np.zeros((50, 100, 1), dtype='uint8')
		cv2.putText(img2,str(vis_dictionary[score[0].argmax()]),(2,45),cv2.FONT_HERSHEY_PLAIN , 1, 255,1)
		cv2.putText(img2,"PREDICTION: ",(2,25),cv2.FONT_HERSHEY_PLAIN , 1, 255,1)
		img = np.array(img * 255, dtype='uint8').reshape(n_rows, n_cols, n_ch)
		img2 = np.concatenate((img, img2), axis=0)

		
		'''
			Show prediction with fancy image pop up, 'q' to quit
		'''
		cv2.imshow("red",img2)
		if cv2.waitKey(0)== 113: 
			break



if __name__ == '__main__':

	if len(sys.argv) == 2 and sys.argv[1] == 't':
		train()
	elif len(sys.argv) == 2 and sys.argv[1] == 'c':
		classify()
	else: 
		print "please specify if you want to 'train : t' or 'classify: c' "




			














