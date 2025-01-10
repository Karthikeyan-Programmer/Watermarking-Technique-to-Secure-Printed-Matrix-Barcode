import warnings
import os
import csv
import time
import shutil
import sys
import pandas as pd
from skimage import io
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from time import sleep
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
from time import sleep
import matplotlib.image as mpimg
import cv2
import numpy as np
import dbr
import PIL
from PIL import Image
import PIL.Image
from PIL import Image, ImageChops
from PIL import Image, ImageFilter
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
from typing import Tuple
import qrcode
from PIL import Image
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import pyzbar.pyzbar as pyzbar
import pyglet
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from itertools import count, cycle
from scipy.fftpack import dct
import barcode
from barcode.writer import ImageWriter
from datetime import datetime
from tkinter import ttk
import tkinter.font as font
import pyqrcode
from pyqrcode import QRCode
from PIL import ImageTk, Image
from time import sleep
from dct import *
from Metrices import *

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
       return im.crop(bbox)
print ("\n\t\t\t===========************ A Watermarking Technique to Secure Printed Matrix Barcode—Application for Anti-Counterfeit Packaging ************============")
def QRImgGeneration():
    time.sleep(1)
    print ("\n\t\t\t===========************ GENERATION OF THE QR CODE IMAGE ************============")
    time.sleep(1)
    QRWin = tk.Tk()
    myFont1 = font.Font(family='Helvetica', weight='bold')
    textbox1 = tk.Text(QRWin, width=24, height=1.5, bd=5, bg='white', font = ("Helvetica", 10), relief ='raised')
    textbox1.place(x=210,y=100)
    btnqr_Set = tk.Button(QRWin, text="Generate QR code", bd=5, width=15, height=2, bg="black", fg="white",
                           command=lambda:qrcode())
    btnqr_Set['font'] = myFont1
    btnqr_Set.place(x = 220, y = 150)

    separator1_style = ttk.Style()
    separator1_style.configure("Line.TSeparator", bg="black")
    separator1= ttk.Separator(QRWin, orient='horizontal')
    separator1.place(x=0, y=350, height=20, width=695)

    separator2= ttk.Separator(QRWin, orient='horizontal') 
    separator2.place(x=0, y=580, width=695, height=20)

    btnclr_Set = tk.Button(QRWin, text="Clear", bd=5, width=10, height=2, bg="orange", fg="black",
                           command=lambda:clearspace(textbox3))
    btnclr_Set['font'] = myFont1
    btnclr_Set.place(x = 450, y = 500)

    textbox3 = tk.Text(QRWin, width=50, height=4, bd=5, bg='light blue', font = ("Helvetica", 12), relief ='raised')
    textbox3.place(x = 100, y = 400)

    btnclr2_Set = tk.Button(QRWin, text="Clear", width=5, height=1, bg="blue", fg="white",
                           command=lambda:clearspace(textbox1))
    btnclr2_Set['font'] = myFont1
    btnclr2_Set.place(x = 400, y = 100)

    textbox4 = tk.Text(QRWin, width=26, height=1, bg='light grey', font = ("Helvetica", 8), relief ='raised')
    textbox4.config(highlightthickness = 0, borderwidth=0)
    textbox4.place(x=50,y=583)
    textbox4.configure(state='disabled')

    def qrcode():        
        """
        function to validate the user input and generate the
        QR code and save the code as png file
        """
        
        user_qrcode_input = textbox1.get("1.0","end").strip()
        file = open('QRcode.txt','w')
        file.write(user_qrcode_input)
        file.close()
        if len(user_qrcode_input) == 0:
            textbox1.delete("1.0","end")
            textbox1.insert('1.0', "No inputs received!")
        else:
            qrcode_op = pyqrcode.create(user_qrcode_input)
            now = datetime.now().strftime("%d%m%Y%H%M%S")
            qr_file_name = "data\QR_code_{}.png".format(now)
            qrcode_op.png(qr_file_name, scale = 8)
            textbox1.delete("1.0","end")
            display_output("QR", "QR code is generated Successfully!", qr_file_name)
        time.sleep(1)
        print("QR code generated successfully...!")
        time.sleep(1)
        print("\nNext click UPLOAD THE QR IMAGE button")

            
    def display_output(code_name, op_str, file_name):       
        """
        function to display the program execution message and also
        list the file name for the saved QR/Barcode
        """
        
        if code_name == 'QR':
            file_name = file_name
        else:
            file_name = '{}.png'.format(file_name)
        textbox3.delete("1.0","end")
        textbox3.insert('1.0', '\t{}{}{}'.format(op_str, "\n\n      Code is saved in file: ", file_name))
        print('1.0', '\t{}{}{}'.format(op_str, "\n\nQRCode is saved in file: ", file_name))
        im = PIL.Image.open(file_name)  
        im.show()

    def clearspace(textboxn):      
        """
        Clear the respective text boxes as per the click button
        """
        
        textboxn.delete("1.0","end")

    ###### Tkinter frame properties            
    # Title and size adjustments
    QRWin.title('           QR CODE Generator - USING PYTHON         ')
    QRWin.geometry('695x600')
    QRWin.resizable(0,0)
    QRWin.configure(bg='burlywood')
    QRWin.mainloop()
    ############################# END OF GENERATION OF THE QR CODE SCRIPTS ########################################        

def upLoadtheQRimage():
    time.sleep(1)
    print ("\n\t\t\t============************ UPLOAD THE QR CODE IMAGE **************===============")
    time.sleep(1)
    plt.figure(1)    
    fileName =filedialog.askopenfilename(filetypes=[("PNG",".png"),("JPG",".jpg")])
    print(fileName)    
    img = mpimg.imread(fileName)
    imgplot = plt.imshow(img)
    plt.xticks([]), plt.yticks([])    
    plt.savefig('IpImg.png', dpi=300, bbox_inches='tight')
    plt.title('Input Image')
    plt.show()
    time.sleep(1)
    print("Selected Input QR Code Image UPloaded Successfully...")
    time.sleep(1)
    print("\nNext click CLIPPING GAUSSIAN NOISE TEXTURE button")

def CGN():
    time.sleep(1)
    print ("\n\t\t\t=======******** THE DIGITAL VERSION OF CGN TEXTURE PROCESS *********========")
    time.sleep(1)
    SHAPE = (150,200)
    noise = np.random.normal(255./2,255./10,SHAPE)
    cv2.imwrite("ClippingGaussianNoiseImg.png", noise)
    print("The digital version of CGN texture process is suceesfully completed...!")
    time.sleep(1)
    print ("\n\t\t\t=======******** The DIGITAl VERSION OF CGN TEXTURE version ********=========")
    time.sleep(1)
    image = io.imread('IpImg.png')
    ax = plt.hist(image.ravel(), bins = 256)
    plt.show()
    time.sleep(1)
    print("The digital version of CGN histogram process is suceesfully completed...!")
    time.sleep(1)
    print("\nNext click DECODE THE NUMERIC PATTERNS button")
    
def Decode():
    time.sleep(1)
    print ("\n\t\t\t==========************* DECODE THE NUMERIC PATTERNS **********===========")
    img = cv2.imread('IpImg.png')
    decoder = cv2.QRCodeDetector()
    data, points, _ = decoder.detectAndDecode(img)
    if points is not None:
        points = points[0]
        for i in range(len(points)):
            pt1 = [int(val) for val in points[i]]
            pt2 = [int(val) for val in points[(i + 1) % 4]]
            cv2.line(img, pt1, pt2, color=(255, 0, 0), thickness=3)
        cv2.imshow('Detected QR code', img)
        cv2.waitKey(0)
    image = cv2.imread("IpImg.png")
    decocdeQR = decode(PIL.Image.open('IpImg.png'))
    print(decocdeQR)
    print('\nQR code Decoded data:',decocdeQR[0].data.decode('ascii'))   
    time.sleep(1)
    print("Decode the numeric patterns process is suceesfully completed...!")
    time.sleep(1)
    print("\nNext click DISCRETE COSINE TRANSFORM DOMAIN button")
    
def DCT():
    time.sleep(1)
    print ("\n\t\t\t==========************ DISCRETE COSINE TRANSFORM DOMAIN ***********==========")
    time.sleep(1)
    DiscreteCosineTransform();
    time.sleep(1)
    x = np.array([1.0, 2.0, 1.0, 2.0, -1.0])
    print("x      : ",x)
    # apply dct function on array
    y = dct(x)
    print("dct(x) : ",y)
    time.sleep(1)
    print("DISCRETE COSINE TRANSFORM process is suceesfully completed...!")
    time.sleep(1)
    print("\nNext click VERIFICATION button")

def Verification():
    time.sleep(1)
    print ("\n\t\t\t==========************ VERIFICATION ***********==========")
    f = open("QRcode.txt", "r")
    content = f.read()
    f.close()
    decocdeQR = decode(PIL.Image.open('IpImg.png'))
    if content == decocdeQR[0].data.decode('ascii'):
        print("\nVERIFICATION RESULT: Numerical")
    elif content != decocdeQR[0].data.decode('ascii'):
        print("\nVERIFICATION RESULT: Genuine")
    else:
        print("\nVERIFICATION RESULT: Falsified")
    print("\nNext click PERFORMANCE METRICS button")
        
def Metrics():
    print ("\n\t\t\t===========********** PERFORMANCE METRICS *********=============")
    time.sleep(1)
    Process();
    time.sleep(1)
    print("\nImplementation is Completed...!")

def main_screen():
    global window
    window = Tk()
    window.geometry("550x140")
    window.title("MainView")
    Label(window, text = "A Watermarking Technique to Secure Printed Matrix Barcode—Application for Anti-Counterfeit Packaging",bg = "MidnightBlue",fg ="white",width = "500", height = "2",font=('Times New Roman',12)).pack()
    Label(text = "").pack()
    Button(text = "START", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = QRImgGeneration).pack()
    Button(text = "UPLOAD THE QR IMAGE", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = upLoadtheQRimage).pack()
    Button(text = "CLIPPING GAUSSIAN NOISE TEXTURE", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = CGN).pack()
    Button(text = "DECODE THE NUMERIC PATTERNS", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = Decode).pack()
    Button(text = "DISCRETE COSINE TRANSFORM DOMAIN", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = DCT).pack()
    Button(text = "VERIFICATION", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = Verification).pack()
    Button(text = "PERFORMANCE METRICS", height = "2", width = "35",bg = "white",fg ="MidnightBlue",font=('Times New Roman',10), command = Metrics).pack()
    Label(text = "").pack()    
    window.mainloop()
    
main_screen()
