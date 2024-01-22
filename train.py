from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")


        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\TD9.jpg")
        img=img.resize((1380,800))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=800) 
        #frame

        main_frame=Frame(f_lbl,bd=2, bg="white")
        main_frame.place(x=50,y=135,width=500,height=500)

        title_lbl=Label(main_frame,text="TRAIN DATA SET",font=("MS Serif",30,"bold"),bg="white",fg='green')
        title_lbl.place(x=0,y=0,width=500,height=100)

        b1_1=Button(main_frame,text="Train Data",command=self.train_clasifier,cursor="hand2",font=("Copperplate",15,"bold"),relief="ridge",bg="forestgreen",fg='white')
        b1_1.place(x=125,y=100,width=220,height=40)

        title_lb=Label(main_frame,text="...Click the above button to Train your data...",font=("MS Serif",14,"bold"),bg="white",fg='maroon')
        title_lb.place(x=0,y=150,width=500,height=50)

        b1_1=Button(main_frame,text="Home",cursor="hand2",font=("Copperplate",15,"bold"),relief="ridge",bg="royalblue",fg='white')
        b1_1.place(x=125,y=210,width=220,height=40)

        img_l=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn17.jpg")
        img_l=img_l.resize((300,300))
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(main_frame,image=self.photoimg_l)
        f_lbl.place(x=115,y=260,width=250,height=250) 

    def train_clasifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #L convert in greyscale
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #==========Train the classifier and save ===========

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed")


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()