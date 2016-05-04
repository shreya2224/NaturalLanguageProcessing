'''
Created on Apr 30, 2016

@author: ShreyaK
'''

import numpy as np
from sklearn import svm
import csv
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

inputfile = open('C:/Users/ShreyaK/workspace/MyPython/output.csv')

inputfile.readline()

data = np.loadtxt(inputfile, delimiter=",")

data_train = data[:,0:2]

print(data_train)

data_label = data[:,2]

print(data_label)

clf = svm.SVC(kernel='linear', C=0.01)

clf.fit(data_train, data_label)
'''
print(clf.predict([1.004,1.5110]))
'''
w = clf.coef_[0]

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(data_train[:, 0], data_train[:, 1], c = data_label)
plt.legend()
plt.show()

storing = []
file1reader = csv.reader(open("C:/Users/ShreyaK/workspace/MyPython/output_cros_val.csv"), delimiter=",")


for prob, sim in file1reader:
    the_row = prob + " " + sim
    
    storing.append(the_row.split())
    
storing.pop(0)

print(storing)
print("labels of test data: ")  
print(clf.predict(storing))


    

    








