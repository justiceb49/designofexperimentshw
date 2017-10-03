# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:14:43 2017

@author: jub061
"""
import sys
import random
import numpy as np

from PyQt5.QtWidgets import (QWidget, QTreeView, QMessageBox, QHBoxLayout, 
                             QFileDialog, QLabel, QSlider, QCheckBox, 
                             QLineEdit, QVBoxLayout, QApplication, QPushButton,
                             QTableWidget, QTableWidgetItem,QSizePolicy,
                             QGridLayout,QGroupBox)
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
import matplotlib.pyplot as plt
from matplotlib.backends import qt_compat
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.mlab as mlab

import scipy.stats as stats

end = 30
end_inner = 1000
binn = 100
sum = []
triangle = []
        
for i in range(0, end):
    y = []
    for j in range(0,end_inner):
        x = random.random()
        y.append(x)
#        print('working...')

    if i == 0:
        sum = y
        
    elif i > 0:
        
        for k in range(0,end_inner):
            sum[k] = sum[k] + y[k]
#            print('k', k, 'sum', sum)

        if i == 1:
            print('This is the 2nd group of random numbers')
            histo1 = plt.hist(y, binn, normed = 1)
            plt.show()
            
        if i == 2:
            triangle = y
            
            
        if i == 3:
            for k in range(0, end_inner):
                triangle[k] = triangle[k] + y[k]
                
            print('This is the triangle distribution')
            histotri = plt.hist(triangle, binn, normed = 1)
            plt.show()
        
        if i == 20:
            print('This is the', 20, 'th group of random numbers' )
            histo2 = plt.hist(y, binn, normed = 1) 
            plt.show()
        
#        else:
#            print(i)
        
#    print('final sum is:',sum, 'i', i)
    sum_array = np.asarray(sum)

mean = np.mean(sum_array)
std = np.std(sum_array)

sum_z = (sum - mean)/std        
    
print('here are the summed lists')    
histo3 = plt.hist(sum, binn, normed = 1)
plt.show()

print('now here is the normalized plot')
histo4 = plt.hist(sum_z, binn, normed = 1)
#x = np.linspace(-3*std, 3*std, end_inner)
s_sum = sorted(sum)
s_sum_z = sorted(sum_z)
y = stats.norm.pdf(s_sum, mean, std)
plot = plt.plot(s_sum_z, y)
plt.show()


print('done')
        
        
