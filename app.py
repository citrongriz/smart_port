import pandas as pd
import numpy as np
import os
#import tensorflow as tf
import cv2

#from tensorflow.keras import models
#from tensorflow.keras import layers
#from tensorflow.keras import optimizers


#from tensorflow.keras import callbacks

#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Reshape
#from  matplotlib import pyplot as plt
#import matplotlib.image as mpimg
#%matplotlib inline
#import random
import streamlit as st
#import pickle
from keras.models import model_from_json

def garbage_pred(predicted_class):
	
	dico = {0:'cardboard' , 1: 'glass', 2: 'metal', 3:'paper' , 4:'plastic' , 5:'trash' }
	x = dico[predicted_class]
	return x

IMG_WIDTH=200
IMG_HEIGHT=200
image =None
opencv_image=None
## load json and create model
json_file = open('notebooks/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
## load weights into new model
loaded_model.load_weights("notebooks/model.h5")
# saving the model 
#pickle_out = open("classifier.pkl", mode = "wb") 
#pickle.dump(model, pickle_out) 
#pickle_out.close()

#pickle_in = open('classifier.pkl', 'rb') 
#classifier = pickle.load(pickle_in)
 


uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','JPG'])


#if uploaded_file is not None:
#    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
#    st.write(file_details)
#    image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)
#    image=cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH),interpolation = cv2.INTER_AREA)
#    image=np.array(image)
#    image = image.astype('float32')
#    image /= 255 


if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    image=cv2.resize(opencv_image, (IMG_HEIGHT, IMG_WIDTH),interpolation = cv2.INTER_AREA)
    image=np.array(image)
    image = image.astype('float32')
    image /= 255
    # Now do something with the image! For example, let's display it:
    st.image(image, channels="BGR")


if image is not None:
	image.shape
	img = np.reshape(image, [1, 200, 200, 3])
	pred =np.argmax(loaded_model.predict(img))
	pred
	prediction_type = garbage_pred(pred)
	prediction_type

