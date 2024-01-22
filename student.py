from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")


        #creating variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       
        #background image
        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\frs2.jpg")
        img=img.resize((1380,900))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=900) 

        #Heading
        title_lbl=Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("Copperplate",35,"bold"),bg="white",fg='black')
        title_lbl.place(x=0,y=90,width=1380,height=45)

        #FRAME
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=0,y=135,width=1500,height=650)

        #left label frame
        l_f=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student Details",font=("times new roman",12,"bold"))
        l_f.place(x=10,y=10,width=660,height=580)

        #left frame image
        img_l=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\frs2.jpg")
        img_l=img_l.resize((1380,900))
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(l_f,image=self.photoimg_l)
        f_lbl.place(x=10,y=0,width=640,height=130) 

        #Current Course
        Current_course=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Currrent course Information",font=("times new roman",12,"bold"))
        Current_course.place(x=15,y=135,width=650,height=130)

        #dep label
        d_l=Label(Current_course,text="Department",font=("times new roman",12,"bold"))
        d_l.grid(row=0,column=0,padx=10)

        d_combo=ttk.Combobox(Current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select ","CS","IT","Civil","Mechanical")
        d_combo.current(0)
        d_combo.grid(row=0,column=1,padx=2,pady=10) 

        #course label
        c_l=Label(Current_course,text="Course",font=("times new roman",12,"bold"))
        c_l.grid(row=0,column=2,padx=10)

        c_combo=ttk.Combobox(Current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        c_combo["values"]=("Select","B.Tech","BE","BSC","BCOM")
        c_combo.current(0)
        c_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W) 

        #year label
        y_l=Label(Current_course,text="Year",font=("times new roman",12,"bold"))
        y_l.grid(row=1,column=0,padx=10)

        y_combo=ttk.Combobox(Current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        y_combo["values"]=("Select","1st year","2nd year","3rd year","4th year")
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester label
        s_l=Label(Current_course,text="Semester",font=("times new roman",12,"bold"))
        s_l.grid(row=1,column=2,padx=10)

        s_combo=ttk.Combobox(Current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        s_combo["values"]=("Select","1","2","3","4","5","6","7","8")
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)  

        #Class student information
        csi=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        csi.place(x=15,y=267,width=650,height=310)

        #Student ID
        student_id=Label(csi,text="Student ID:",font=("times new roman",12,"bold"))
        student_id.grid(row=0,column=0,padx=10,pady=5)

        studentid_entry=ttk.Entry(csi,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #Student name
        student_name=Label(csi,text="Student name:",font=("times new roman",12,"bold"))
        student_name.grid(row=0,column=2,padx=10,pady=5)

        studentname_entry=ttk.Entry(csi,textvariable=self.var_name, width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Class Divison
        class_divison=Label(csi,text="Class Divison:",font=("times new roman",12,"bold"))
        class_divison.grid(row=1,column=0,padx=10,pady=5)

        cd_entry=ttk.Entry(csi,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        cd_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #Roll number
        rn=Label(csi,text="Roll number:",font=("times new roman",12,"bold"))
        rn.grid(row=1,column=2,padx=10,pady=5)

        rn_entry=ttk.Entry(csi,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rn_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Gender
        gender=Label(csi,text="Gender:",font=("times new roman",12,"bold"))
        gender.grid(row=2,column=0,padx=10,pady=5)
        
        g_combo=ttk.Combobox(csi,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        g_combo["values"]=("Select","Female","Male","Transgender","Others")
        g_combo.current(0)
        g_combo.place(width=167,height=28, x=133,y=73)
     
        #DOB
        dob=Label(csi,text="Date of Birth:",font=("times new roman",12,"bold"))
        dob.grid(row=2,column=2,padx=10,pady=5)

        db_entry=ttk.Entry(csi,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        db_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #Email
        email=Label(csi,text="Email:",font=("times new roman",12,"bold"))
        email.grid(row=3,column=0,padx=10,pady=5)

        email_entry=ttk.Entry(csi,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #Phone no.
        ph=Label(csi,text="Phone number:",font=("times new roman",12,"bold"))
        ph.grid(row=3,column=2,padx=10,pady=5)

        ph_entry=ttk.Entry(csi,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        ph_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #Address
        add=Label(csi,text="Address:",font=("times new roman",12,"bold"))
        add.grid(row=4,column=0,padx=10,pady=5)

        add_entry=ttk.Entry(csi,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        #Teacher name
        tn=Label(csi,text="Teacher name:",font=("times new roman",12,"bold"))
        tn.grid(row=4,column=2,padx=10,pady=5)

        tn_entry=ttk.Entry(csi,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        tn_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(csi,text="Take photo sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(csi,text="No photo sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=1)

        btn_frame=Frame(csi,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=645, height=35)

        #Save , update delete button

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(csi,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=250,width=645, height=35)

        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=0,column=1)

        #right label frame
        r_f=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        r_f.place(x=680,y=10,width=660,height=580)

        #right frame image
        img_2=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\frs5.jpg")
        img_2=img_2.resize((1080,500))
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        f_lbl=Label(r_f,image=self.photoimg_2)
        f_lbl.place(x=10,y=0,width=640,height=130)
       
        #Search system
        search=LabelFrame(r_f,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search.place(x=10,y=130,width=640,height=70)

        searchbar=Label(search,text="Search By : ",font=("times new roman",12,"bold"), bg="plum",relief="ridge")
        searchbar.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search,font=("times new roman",12,"bold"),state="readonly", width=15)
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        search_entry=ttk.Entry(search,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=2)
        
        search_btn=Button(search,text="Search",width=10,font=("times new roman",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        #Table frame
        table_f=Frame(r_f,bd=2,relief=RIDGE)
        table_f.place(x=10,y=210,width=640,height=325)

        scroll_x=ttk.Scrollbar(table_f,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_f,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_f,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #set the heading of table
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("roll",text="Rollnumber")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
         
        # setting width of column
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) # bind to ip and port to so that it can listen to incoming request
        self.fetch_data()

        # FUNCTION DECLARATION=============
    def add_data(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
            try:
                conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
                my_cursor=conn.cursor()  #cursor allow to run sql command from python, cursor point the result or data generated
                my_cursor.execute("insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),
                    self.var_year.get(),self.var_semester.get(),self.var_id.get(),self.var_name.get(),self.var_div.get(),self.var_roll.get(),
                    self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                    self.var_teacher.get(),self.var_radio1.get()))
                conn.commit()   #modify data for tables after transaction 
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    # fetching data from database
    def fetch_data(self):
        conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()  #for adding data
        conn.close()
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()  #focus on the accepting input window
        content=self.student_table.item(cursor_focus) #it return the list with all values
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),
    
    # update the data ==============
    def update_data(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student1 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s Where Student_ID=%s",(self.var_dep.get(),self.var_course.get(),
                    self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_div.get(),self.var_roll.get(),
                    self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                    self.var_teacher.get(),self.var_radio1.get(),self.var_id.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            #====FUNCTION FOR DELETING THE DATA=============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be requires",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
                    my_cursor=conn.cursor()
                    sql="delete from student1 where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

     #=======RESET FUNCTION====================
    def reset_data(self):
        self.var_dep.set("Select"),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),

    #===========Generate dataset or take photo samples================
    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required!!",parent=self.root)
        else:
            try:
                conn=mysql.connector.Connect(host="localhost",username="root",password="12345",database="face_recognizer1")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1")  #select the data and then store it to myresult
                myresult=my_cursor.fetchall()
                id=0             #creating id for photo samples
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student1 set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s Where Student_ID=%s",(self.var_dep.get(),self.var_course.get(),
                    self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_div.get(),self.var_roll.get(),
                    self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),
                    self.var_teacher.get(),self.var_radio1.get(),self.var_id.get()==int(id)+1))  
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # LOAD PREDIFIEND DATA ON DACE FRONTALS FORM OPENCV============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  #for loading file

                def face_cropped(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                    faces=face_classifier.detectMultiScale(grey,1.3,5)           #scaling factor=1.3 , Minimum neighbour=5 return a boundary rectangles for detecting
                    for(x,y,w,h) in faces:                                       #loop for covering the boundary
                        face_cropped=img[y:y+h,x:x+w]                            #for drawing a rectangle around the boundary
                        return face_cropped
                cap=cv2.VideoCapture(0)                                          #capture video object
                img_id=0
                while True:                                                      #running infinite loop 
                    ret,myframe=cap.read()                                       #read all frames in captures video
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))  
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filenamepath="data/user."+str(id)+"."+str(img_id)+".jpg"  #image name should be this format
                        cv2.imwrite(filenamepath,face)                            #saved the image in a specified file
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)                           #show the resulting frame

                    if cv2.waitKey(1)==ord('q') or int(img_id)==100:
                        break                                                     #break the loop when this condition is true
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("RESULT","Generating data sets completed !!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()