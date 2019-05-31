import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
from sklearn.model_selection import train_test_split
from keras import callbacks
from keras.utils import to_categorical
from keras_lr_finder import LRFinder

#loads and formats data
data = np.loadtxt("data.csv", delimiter=",")
X = data[:,0:8]
Y = data[:,8]

#train test splits
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

#model architecture
model = Sequential()
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam", metrics=["mean_absolute_error"])
#model.fit(x_train, y_train, epochs=0)
#custom callback to print learning rate
class MyCallback(callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        print(K.eval(self.model.optimizer.lr))

#learning rate search
# model is a Keras model
lr_finder = LRFinder(model)


#searches learning rates from 0.00001 to 1 and plots loss
lr_finder.find(x_train, y_train, start_lr=0.00001, end_lr=1, batch_size=64, epochs=20)
lr_finder.plot_loss()

#gets a region to zoom in on
min_lr  = float(input("Enter the lowest learning rate to show    "))
max_lr  = float(input("Enter the highest learning rate to show    "))

#same again but with the new region
lr_finder = LRFinder(model)
lr_finder.find(x_train, y_train, start_lr=min_lr, end_lr=max_lr, batch_size=64, epochs=20)
lr_finder.plot_loss(x_scale="linear")

#gets the learning rate to train with
lr  = float(input("Enter the learning rate to use    "))

K.set_value(model.optimizer.lr, lr)
#reduces learning rate when val_loss stagnates         
ReduceLR = callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.85, verbose=0, cooldown=30, min_lr=0.0001)
#saves the best model based on val_loss with the name of the val_acc rounded to 2 decimal places
savebest = callbacks.ModelCheckpoint(filepath="checkpoint-{val_mean_absolute_error:.2f}.h5", monitor="val_loss", save_best_only=True)
tb = callbacks.TensorBoard(log_dir='/tmp/tb/', write_graph=True)
PrintLR = MyCallback()
callbacks_list = [ReduceLR, PrintLR, savebest, tb]

#trains the model for 10,000 epochs but it should probably be stopped earlier by a keyboard interrupt
model.fit(x_train, y_train, epochs=1000, batch_size=64, validation_data=(x_test, y_test), callbacks=callbacks_list)

K.clear_session()
