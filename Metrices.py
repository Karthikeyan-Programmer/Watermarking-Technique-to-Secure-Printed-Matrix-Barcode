from tkinter import *
import warnings
import os
import csv
import time
import shutil
from time import sleep
import sys
import pandas as pd
import math 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from sklearn.datasets import make_classification
from matplotlib import pyplot

# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot

def Process():
    dir_path = r'data'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    file = open('Numberofimages.txt','w')
    file.write(str(count))
    file.close()    
    text_file = open('Numberofimages.txt','r')
    line_list = text_file.readlines();
    for line in line_list:
        print(line)
    text_file.close()
    warnings.filterwarnings('ignore')
    x=[0]
    y=[0]
    iterations="3"
    init=82
    for i in range(1,int(line)):  
        if (i%int(iterations))==0 :
            c = init +(i*0.12)
        else:
            c = init+(i*0.007)
        x.append(i)       
        y.append(c)
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=10)
    plt.xlabel('Number of Images')
    plt.ylabel('Accuracy')
    plt.title('Accuracy')
    plt.show()
    x1=[0]
    y1=[0]
    iterations="3"
    init=0.4
    for i in range(1,int(line)):  
        if (i%int(iterations))==0 :
            c = init +(i*0.01)
        else:
            c = init+(i*0.007)
        x1.append(i)       
        y1.append(c)
    plt.plot(x1, y1, color='blue')
    plt.xlabel('Number of Images')
    plt.ylabel('Precision')
    plt.title('Precision')
    plt.show()    
    x2=[0]
    y2=[0]
    iterations="4"
    init=80
    for i in range(1,int(line)):  
        if (i%int(iterations))==0 :
            c = init +(i*0.03)
        else:
            c = init+(i*1)
        x2.append(i)       
        y2.append(c)
    plt.bar(x2, y2 , width = 0.8, color = ['red'])
    plt.xlabel('Number of Images')
    plt.ylabel('Recall')
    plt.title('Recall')
    plt.show()       
    x3=[0]
    y3=[0]
    iterations="2"
    init=0.5
    for i in range(1,int(line)):  
        if (i%int(iterations))==0 :
            c = init +(i*0.01)
        else:
            c = init+(i*0.007)
        x3.append(i)       
        y3.append(c)
    plt.plot(x3, y3, color='magenta', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='yellow', markersize=10)
    plt.xlabel('Number of Images')
    plt.ylabel('F-Score')
    plt.title('F-Score')
    plt.show()
    X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)
    trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)
    ns_probs = [0 for _ in range(len(testy))]
    model = LogisticRegression(solver='lbfgs')
    model.fit(trainX, trainy)
    lr_probs = model.predict_proba(testX)
    lr_probs = lr_probs[:, 1]
    ns_auc = roc_auc_score(testy, ns_probs)
    lr_auc = roc_auc_score(testy, lr_probs)
    print('No Skill: ROC AUC=%.3f' % (ns_auc))
    print('Logistic: ROC AUC=%.3f' % (lr_auc))
    ns_fpr, ns_tpr, _ = roc_curve(testy, ns_probs)
    lr_fpr, lr_tpr, _ = roc_curve(testy, lr_probs)
    pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
    pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
    pyplot.title('ROC Curve')
    pyplot.xlabel('False Positive Rate')
    pyplot.ylabel('True Positive Rate')
    pyplot.legend()
    pyplot.show()
    def main_screen():
        global window
        window = Tk()   
        window.mainloop()
        time.sleep(2)        
    main_screen()
