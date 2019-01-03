import numpy as np
from keras.models import load_model

#loads the model
model=load_model("model.h5")

#gets the data we will be basing our prediction on
gender=input("Male, female or infant?    ")
shell_length=float(input("How many mm wide is the shell at it's widest point?     "))
diameter=float(input("How many mm is the shell at the point perpendicular to the widest point?    "))
height=float(input("How high is the in shell with meat in mm?    "))
weight=float(input("How heavy is the whole abalone in grams?    "))
meat_weight=float(input("How heavy is the meat in grams?    "))
organ_weight=float(input("How heavy is the guts after bleeding?    "))
shell_weight=float(input("How heavy is the shell after drying?    "))

if gender[0].upper()=="M":
    gender=1
elif gender[0].upper()=="F":
    gender=2
elif gender[0].upper()=="I":
    gender=0
    
#puts the data into the required format
data=np.array([[gender, shell_length, diameter, height, weight, meat_weight, organ_weight, shell_weight]])
#makes a prediction
age=model.predict(data)[0][0]
print("It is",age,"years old")
