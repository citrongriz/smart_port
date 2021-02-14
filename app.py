import pandas as pd
import numpy as np
import os
import tensorflow as tf
import cv2

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers


from tensorflow.keras import callbacks

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Reshape
from  matplotlib import pyplot as plt
import matplotlib.image as mpimg
#%matplotlib inline
import random
import streamlit as st
import pickle
#from keras.models import model_from_json



## load json and create model
#json_file = open('notebooks/model.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
## load weights into new model
#loaded_model.load_weights("notebooks/model.h5")
# saving the model 
#pickle_out = open("classifier.pkl", mode = "wb") 
#pickle.dump(model, pickle_out) 
#pickle_out.close()

#pickle_in = open('classifier.pkl', 'rb') 
#classifier = pickle.load(pickle_in)
 


uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)