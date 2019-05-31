# abalone-ai
This is my first use of Keras for regression instead of classification and now features semi-automated learning rate search. All you have to do is aim for a learning rate that is a little bit before a sharp decrease in the graph.  
This a pipeline from data visualisation to data balancing to model training to prediction on the [UCL Abalone dataset](https://archive.ics.uci.edu/ml/datasets/abalone)  
I have achived a mean error of ±1.473 years train and ±1.462 years test  
Feedback and pull requests are very welcome

## Copyright
Copyright © 2019  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a summary of the licence go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)

## Prerequisites
### For One Liner
* Curl `apt-get install curl`
### For Manual Install
* [Python 3](https://www.python.org/downloads/)
* Keras `pip install keras`
* Numpy `pip install numpy`
* TensorFlow `pip install tensorflow`
* Scikit-Learn `pip install sklearn`
* h5py `pip install h5py`
* [keras_lr_finder](https://github.com/qwertpi/keras_lr_finder)
* libhdf5 (needed on Linux only) `sudo apt-get install libhdf5-serial-dev`
