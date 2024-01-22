from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import os
import csv

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")

         #creating variables
        self.var_dep=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

        #background image
        img=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\tve.png")
        img=img.resize((1380,900))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1380,height=900) 

        #Heading
        title_lbl=Label(f_lbl,text="STUDENT ATTENDANCE DETAIL",font=("Copperplate",35,"bold"),bg="white",fg='black')
        title_lbl.place(x=0,y=90,width=1380,height=45)

        #FRAME
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=0,y=135,width=1500,height=650)

        #left label frame
        l_f=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student Attendance Details",font=("times new roman",12,"bold"))
        l_f.place(x=10,y=10,width=660,height=580)

        #left frame image
        img_l=Image.open(r"C:\Users\Acer\Desktop\face recognition system\frs images\tea1.jpg")
        img_l=img_l.resize((700,350))
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_lbl=Label(l_f,image=self.photoimg_l)
        f_lbl.place(x=10,y=0,width=640,height=180)

        #Class student information
        csi=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),bg="white")
        csi.place(x=15,y=220,width=650,height=365) 

        #Student ID
        student_id=Label(csi,text="Student ID:",font=("times new roman",12,"bold"))
        student_id.grid(row=0,column=0,padx=10,pady=5)

        studentid_entry=ttk.Entry(csi,width=20,textvariable=self.var_id,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #Student name
        student_name=Label(csi,text="Student name:",font=("times new roman",12,"bold"))
        student_name.grid(row=0,column=2,padx=10,pady=5)

        studentname_entry=ttk.Entry(csi, textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Class Dep
        class_divison=Label(csi,text="Department:",font=("times new roman",12,"bold"))
        class_divison.grid(row=1,column=0,padx=10,pady=5)

        cd_entry=ttk.Entry(csi,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        cd_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #Roll number
        rn=Label(csi,text="Roll number:",font=("times new roman",12,"bold"))
        rn.grid(row=1,column=2,padx=10,pady=5)

        rn_entry=ttk.Entry(csi,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rn_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Class time
        class_divison=Label(csi,text="Time:",font=("times new roman",12,"bold"))
        class_divison.grid(row=2,column=0,padx=10,pady=5)

        cd_entry=ttk.Entry(csi,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        cd_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #Roll date

        rn=Label(csi,text="Date:",font=("times new roman",12,"bold"))
        rn.grid(row=2,column=2,padx=10,pady=5)

        rn_entry=ttk.Entry(csi,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        rn_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        gender=Label(csi,text="Attendance Status:",font=("times new roman",12,"bold"))
        gender.grid(row=3,column=0,padx=10,pady=5)
        
        g_combo=ttk.Combobox(csi,font=("times new roman",12,"bold"),textvariable=self.var_attendance,state="readonly")
        g_combo["values"]=("Status","Present","Absent")
        g_combo.current(0)
        g_combo.place(width=167,height=28, x=163,y=110)

        btn_frame=Frame(csi,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=645, height=35)

        #Save , update delete button

        save_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
     

        #right label frame
        r_f=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        r_f.place(x=680,y=10,width=660,height=580)

        #Table frame
        table_f=Frame(r_f,bd=2,relief=RIDGE,bg="white")
        table_f.place(x=10,y=6,width=640,height=540)

        scroll_x=ttk.Scrollbar(table_f,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_f,orient=VERTICAL)
        self.Attendance_table=ttk.Treeview(table_f,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("id",text="Attendance ID")
        self.Attendance_table.heading("roll",text="Roll Number")
        self.Attendance_table.heading("name",text="Name")
        self.Attendance_table.heading("department",text="Department")
        self.Attendance_table.heading("time",text="Time")
        self.Attendance_table.heading("date",text="Date")
        self.Attendance_table.heading("attendance",text="Attendance")

        self.Attendance_table["show"]="headings"  #remove a invisible first column

        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("roll",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("department",width=100)
        self.Attendance_table.column("time",width=100)
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("attendance",width=100)

        self.Attendance_table.pack(fill=BOTH,expand=1)

        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("",END,values=i)
    
    def importcsv(self):
        global mydata
        mydata.clear()
        files=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with open(files) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #===================Export CSV====================
    
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found to Export!",parent=self.root)
                return False
            files=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
            with open(files,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(files)+" Sucessfully!!")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")





if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()