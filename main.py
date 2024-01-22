from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recog import Face_recog
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background image
        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\frs2.jpg")
        img=img.resize((1380,900))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=900) 

        #Heading
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Copperplate",35,"bold"),bg="white",fg='black')
        title_lbl.place(x=0,y=90,width=1380,height=45)


        #Student button
        img1=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn7.jpg")
        img1=img1.resize((220,220))
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(f_lbl,image=self.photoimg1,cursor="hand2",command=self.student_details)
        b1.place(x=120,y=200,width=220,height=220)

        b1_1=Button(f_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=120,y=380,width=220,height=40)

        #Face Detector
        img2=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn8.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(f_lbl,image=self.photoimg2,command=self.face_data,cursor="hand2")
        b1.place(x=420,y=200,width=220,height=220)

        b1_1=Button(f_lbl,text="Face Detector",command=self.face_data,cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=420,y=380,width=220,height=40)

       #Attendance 
        img3=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn13.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(f_lbl,image=self.photoimg3,command=self.attendance_data,cursor="hand2")
        b1.place(x=720,y=200,width=220,height=220)

        b1_1=Button(f_lbl,text="Attendance",command=self.attendance_data,cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=720,y=380,width=220,height=40)  
         
        #help button
        img4=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn19.png")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_lbl,image=self.photoimg4,cursor="hand2")
        b1.place(x=1020,y=200,width=220,height=220)

        b1_1=Button(f_lbl,text="Help Desk",cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=1020,y=380,width=220,height=40)

        #Train data
        img5=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn12.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(f_lbl,image=self.photoimg5,cursor="hand2",command=self.Training_data)
        b1.place(x=120,y=450,width=220,height=220)

        b1_1=Button(f_lbl,text="Train Data",cursor="hand2",command=self.Training_data,font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=120,y=630,width=220,height=40)

        #photos data
        img6=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn15.png")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_lbl,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1.place(x=420,y=450,width=220,height=220)

        b1_1=Button(f_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=420,y=630,width=220,height=40)

        #Developer
        img7=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn17.jpg")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_lbl,image=self.photoimg7,cursor="hand2")
        b1.place(x=720,y=450,width=220,height=220)

        b1_1=Button(f_lbl,text="Developer",cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=720,y=630,width=220,height=40)

        #Exit
        img8=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn7.jpg")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_lbl,image=self.photoimg8,cursor="hand2")
        b1.place(x=1020,y=450,width=220,height=220)

        b1_1=Button(f_lbl,text="Exit",cursor="hand2",font=("Copperplate",15,"bold"),bg="white",fg='black')
        b1_1.place(x=1020,y=630,width=220,height=40)
       
       #for opening the folder data through photos button
    def open_img(self):
        os.startfile("data")

        #  FUNCTION for student details tab

    def student_details(self):
        self.app=Student(Toplevel(self.root))

    def Training_data(self):
        self.app=Train(Toplevel(self.root))

    def face_data(self):
        self.app=Face_recog(Toplevel(self.root))

    def attendance_data(self):
        self.app=Attendance(Toplevel(self.root))



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()