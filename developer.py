from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\frs4.jpg")
        img=img.resize((1380,750))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=750) 

        #left label frame
        l_f=LabelFrame(f_lbl,bd=2,relief=RIDGE,bg="white",text="Profile",font=("times new roman",12,"bold"))
        l_f.place(x=80,y=75,width=300,height=580)


        img_l=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\dee.jpeg")
        img_l=img_l.resize((250,250))
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(l_f,image=self.photoimg_l)
        f_lbl.place(x=15,y=5,width=260,height=260)

        d_l=Label(l_f,text="🐍 Python Developer | 🎓 CS Student",font=("times new roman",12,"bold"),bg="white")
        d_l.place(x=17,y=274)

        b_l=Label(l_f,text="💻 Code Enthusiast",font=("times new roman",12,"bold"),bg="white")
        b_l.place(x=70,y=300)

        a_l=Label(l_f,text="🌐 Constantly learning and building",font=("times new roman",12,"bold"),bg="white",fg="blue")
        a_l.place(x=17,y=330)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()