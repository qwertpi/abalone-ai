# abalone-ai
This is my first use of Keras for regression instead of classification  
This a pipeline from data visualisation to data balancing to model training to prediction on the [UCL Abalone dataset](https://archive.ics.uci.edu/ml/datasets/abalone)  
I have achived a mean error of ±1.473 years train and ±1.462 years test  
Feedback and pull requests are very welcome

## Plots of data
![Column 1](Figure_1.png?raw=true "Column 1")
![Column 1 balanced](Figure_1_balanced.png?raw=true "Column 1 balanced")
![Column 2](Figure_2.png?raw=true "Column 2")
![Column 3](Figure_3.png?raw=true "Column 3")
![Column 4](Figure_4.png?raw=true "Column 4")
![Column 5](Figure_5.png?raw=true "Column 5")
![Column 6](Figure_6.png?raw=true "Column 6")
![Column 7](Figure_7.png?raw=true "Column 7")
![Column 8](Figure_8.png?raw=true "Column 8")
![Age](Figure_age.png?raw=true "Age")

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
* libhdf5 (needed on Linux only) `sudo apt-get install libhdf5-serial-dev`
## One Liner Install (Linux Only)
` curl https://raw.githubusercontent.com/qwertpi/iris-ai/master/install.bash | sudo bash `
