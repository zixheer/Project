import numpy as np
import streamlit as st
import servo_control as controls
from time import sleep
import cv2
import os
from capture_img import capture_fruit
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

# Load the VGG-16 model
model = load_model("Fresh_Rotten_Fruit_VGG16_Model.h5")

#capture image
capture_fruit()

# Load and preprocess the image
img_path = "fruit.jpg"
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make a prediction
preds = model.predict(x)
fruitP = np.argmax(preds[0])

# Define the class labels
class_labels = {
    0: 'fresh apples',
    1: 'fresh banana',
    2: 'fresh orange',
    3: 'defected apple',
    4: 'defected banana',
    5: 'defected orange'
}

# Get the predicted class label
predicted_class = class_labels[fruitP]

# print the predicted class
st.write("Predicted class:", predicted_class)
print("Predicted class:", predicted_class)

# Display the image
img_array = np.array(img)
st.image(img_array, caption="Inputted Fruit Image", use_column_width=True)

# Machine starts
if fruitP in [0, 1, 2]:  # Assuming 0 represents rotten oranges, 1 represents rotten apples, and 2 represents rotten banana
    controls.raiseLift()
    sleep(4)
    controls.lowerLift()
else:
    controls.raiseFirstHand()
    sleep(5)
    controls.lowerFirstHand()
    sleep(5)
