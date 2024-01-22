from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recog:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\TD3.jpg")
        img=img.resize((1380,750))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=750) 

        #Frame
        main_frame=Frame(f_lbl,bd=2, bg="white")
        main_frame.place(x=50,y=135,width=500,height=500)

        title_lbl=Label(main_frame,text="FACE RECOGNITION",font=("MS Serif",30,"bold"),bg="white",fg='green')
        title_lbl.place(x=0,y=0,width=500,height=100)

        b1_1=Button(main_frame,text="Press",command=self.face_recog1,cursor="hand2",font=("Copperplate",15,"bold"),relief="ridge",bg="forestgreen",fg='white')
        b1_1.place(x=125,y=100,width=220,height=40)

        title_lb=Label(main_frame,text="...Click the above button to Recognising Your Face...",font=("MS Serif",14,"bold"),bg="white",fg='maroon')
        title_lb.place(x=0,y=150,width=500,height=50)

        b1_1=Button(main_frame,text="Home",cursor="hand2",font=("Copperplate",15,"bold"),relief="ridge",bg="royalblue",fg='white')
        b1_1.place(x=125,y=210,width=220,height=40)

        img_l=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\bn17.jpg")
        img_l=img_l.resize((300,300))
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(main_frame,image=self.photoimg_l)
        f_lbl.place(x=115,y=260,width=250,height=250) 
   #===================ATTENDANCE=======================
    def mark_attendance(self,a,r,n,d):
        with open("markattendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))  #example-- deeksha,12,csb
                name_list.append(entry[0])
            if((a not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{a},{r},{n},{d},{dtString},{d1},Present")

   #===============FACE RECOGNITION=====================
    def face_recog1(self):
        def draw_boundray(img,classifier,scaleFactor,miniNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,miniNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student1 where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)   #for concatination

                my_cursor.execute("select Roll from student1 where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)   #for concatination

                my_cursor.execute("select Dep from student1 where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)   #for concatination

                my_cursor.execute("select Student_ID from student1 where Student_ID="+str(id))
                a=my_cursor.fetchone()
                a="+".join(a)   #for concatination


                if confidence>77:
                    cv2.putText(img,f"ID:{a}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(a,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()