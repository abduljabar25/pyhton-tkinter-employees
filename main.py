import sqlite3
from  tkinter import *
import tkinter.messagebox as tkMessageBox
from  tkinter import ttk
import datetime as dt
import tkcalendar

from tkinter import messagebox
import datetime
now = datetime.datetime.utcnow()
mydata=[]
class Employees:

    #-------------------انشاء نافذة البرنامج------------
    def __init__(self,root):
        self.root = root
        self.root.title('برنامج ادارة الموارد البشرية')
        self.root.geometry('1350x690+1+1')
        self.root.configure(bg='#bd9354')
        self.root.iconbitmap('mn.ico')
        self.root.resizable(False,False)
        title=Label(self.root,bg='#92967d',fg='white',text='ادارة الموظفين')
        title.pack(fill='x')

        #---------------------------varibals-----------------------------------
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.Career_var=StringVar()
        self.Academic_var=StringVar()
        self.Date_var=StringVar()
        self.serves_var=StringVar()
        self.Degree_var=StringVar()
        self.Stage_var=StringVar()
        self.Both_var=StringVar()
        self.premium_var=StringVar()
        self.upgrading_var=StringVar()
        self.search_by=StringVar()
        self.search_var=StringVar()
        self.dele_var=StringVar()

        # ---------------------------ادوات التحكم بالبرنامج(النافذه على اليمين)--------------------
        M_Frame= Frame(self.root,bg='#e3d18a')
        M_Frame.place(x=1139,y=20,width=210,height=465)
        lb1_ID=Label(M_Frame,bg='#e3d18a',text='الرقم الوظيفي')
        lb1_ID.pack()
        Id_Entry=Entry(M_Frame,textvariable=self.id_var,bd='2',justify='center')
        Id_Entry.pack()
        lb2 = Label(M_Frame, bg='#e3d18a', text='اسم الموظف')
        lb2.pack()
        name_Entry = Entry(M_Frame, bd='2',justify='center',textvariable=self.name_var, validate="focusout")
        name_Entry.pack()
        lb3= Label(M_Frame , bg='#e3d18a', text='العنوان الوظيفي')
        lb3.pack()
        Career_Title=Entry(M_Frame, bd='2',justify='center',textvariable=self.Career_var)
        Career_Title.pack()
        lb4 = Label(M_Frame, bg='#e3d18a', text='التحصيل الدراسي')
        lb4.pack()
        com_Academic = ttk.Combobox(M_Frame, justify='center',state="readonly",textvariable=self.Academic_var)
        com_Academic['value']=('امي','يقرا ويكتب','ابتدائية','متوسطة','اعدادية','دبلوم','بكلوريوس','ماجستير','دبلوم عالي','دكتوراة')
        com_Academic.pack()
        lb5 = Label(M_Frame, bg='#e3d18a', text='تاريخ التعيين')
        lb5.pack()
        Date_of_hiring = tkcalendar.DateEntry(M_Frame, textvariable=self.Date_var, date_pattern='y/mm/dd', bd='2', justify='center')
        Date_of_hiring.pack()
        lb6 = Label(M_Frame, bg='#e3d18a', text='الخدمة المضافة')
        lb6.pack()
        serves_add = Entry(M_Frame, bd='2', justify='center',textvariable=self.serves_var)
        serves_add.pack()
        lb7 = Label(M_Frame, bg='#e3d18a', text='الدرجة')
        lb7.pack()
        Degree = ttk.Combobox(M_Frame, justify='center',textvariable=self.Degree_var,state="readonly")
        Degree['value'] = ('الاولى', 'الثانية', 'الثالثة','الرابعة','الخامسة', 'السادسة','السابعة','الثامنة', 'التاسعة','العاشرة')
        Degree.pack()
        lb8 = Label(M_Frame, bg='#e3d18a', text='المرحلة')
        lb8.pack()
        Stage = ttk.Combobox(M_Frame, justify='center',textvariable=self.Stage_var,state="readonly")
        Stage['value'] = ('الاولى', 'الثانية','الثالثة','الرابعة','الخامسة','السادسة','السابعة','الثامنة','التاسعة','العاشرة','الحادية عشر')
        Stage.pack()
        lb9 = Label(M_Frame, bg='#e3d18a', text='كتب الشكر')
        lb9.pack()
        Both = Entry(M_Frame, bd='2', justify='center',textvariable=self.Both_var)
        Both.pack()
        lb10 = Label(M_Frame, bg='#e3d18a', text='تاريخ اخر علاوه')
        lb10.pack()
        premium = tkcalendar.DateEntry(M_Frame, bd='2', justify='center', state="readonly", date_pattern='y/mm/dd', textvariable=self.premium_var)
        premium.pack()
        lb11 = Label(M_Frame, bg='#e3d18a', text='تاريخ اخر ترفيع')
        lb11.pack()
        upgrading = tkcalendar.DateEntry(M_Frame, bd='2', justify='center', state="readonly", date_pattern='y/mm/dd', textvariable=self.upgrading_var)
        upgrading.pack()


#------------------------buttons-------------------------------
        btn_Fram=Frame(self.root,bg='#85603f')
        btn_Fram.place(x=1139,y=485,width=210,height=253)
        title1=Label(btn_Fram ,font=('Deco',14),fg='red',bg='#92967d',text='لوحة التحكم')
        title1.pack(fill='x')
        add_btn=Button(btn_Fram, text='اضافة موظف',bg='#bd9354',command=self.add_Employees)
        add_btn.place(x=33,y=33 ,width=150,height=25)
        update_btn=Button(btn_Fram, text='تعديل بيانات الموظف',bg='#bd9354',command=self.updeat)
        update_btn.place(x=33, y=60, width=150, height=25)
        clear_btn=Button(btn_Fram, text='تفريغ الحقول',bg='#bd9354',command=self.clear)
        clear_btn.place(x=33, y=87, width=150, height=25)
        about_btn = Button(btn_Fram, text='برمجة وتصميم', bg='#bd9354',command=self.coding)
        about_btn.place(x=33, y=114, width=150, height=25)
        exit_btn=Button(btn_Fram, text='اغلاق البرنامج',bg='#bd9354',command=self.Exit)
        exit_btn.place(x=33, y=141, width=150, height=25)
        lib_version=Label(btn_Fram, text='اصدار البرنامج 1.0.0',bg='#85603f',fg = "white")
        lib_version.place(x=33, y=180, width=150, height=25)
#-------------------------------search-----------------
        search_Fram=Frame(self.root,bg='#c8c6a7')
        search_Fram.place(x=0,y=20,width=1139,height=50)
        lb1_search=Label(search_Fram,bg='#c8c6a7',text='البحث عن الموظف')
        lb1_search.place(x=1034,y=12)
        w = Label(root, text=f"{dt.datetime.now():'%Y/%m/%d %I:%M:%S %p'}", fg="#85603f", bg="#c8c6a7", font=("helvetica", 10))
        w.pack()
        searc_Entry=Entry(search_Fram,bd='2', justify='center',textvariable=self.search_var)
        searc_Entry.place(x=880,y=12)
        sear_bt=Button(search_Fram ,text='بحث',bg='#85603f',fg = "white",command=self.search)
        sear_bt.place(x=815,y=12,width=50,height=25)
        sear_end = Button(search_Fram, text='انهاء البحث', bg='#85603f', fg="white",command=self.fetch_all)
        sear_end.place(x=750, y=12, width=60, height=25)
     #---------------------delete ----------------------------
        lb1_del = Label(search_Fram, bg='#c8c6a7', text='حذف موظف')
        lb1_del.place(x=260, y=12)
        dele_Entry = Entry(search_Fram, bd='2', justify='center',textvariable=self.dele_var)
        dele_Entry.place(x=125, y=12)
        dele_bt = Button(search_Fram, text='حذف', bg='#85603f', fg="white", command=self.delmployee)
        dele_bt.place(x=50, y=12,width=50,height=20)
        #------------------------------------------عرض بيانات الموظف--------------------
        Dietals_Fram=Frame(self.root,bg='#c8c6a7')
        Dietals_Fram.place(x=1,y=82,width=1134,height=605)
        scroll_x=Scrollbar(Dietals_Fram,orient= HORIZONTAL)
        scroll_y = Scrollbar(Dietals_Fram, orient=VERTICAL)
        self.employees_table=ttk.Treeview(Dietals_Fram,
        columns = ('upgrading_var', 'premium_var', 'Both_var','Stage_var','Degree_var','serves_var','Date_var',
                   'Academic_var','Career_var','name_var','id_var'), selectmode="extended", height=900,
        xscrollcommand =scroll_x.set,
        yscrollcommand=scroll_y.set  )
        self.employees_table.place(x=18,y=1,width=1130,height=587 )
        scroll_x.pack(side=BOTTOM,fill='x')
        scroll_y.pack(side=LEFT,fill='y')
        scroll_x.config(command=self.employees_table.xview)
        scroll_y.config(command=self.employees_table.yview)

        style = ttk.Style()
        style.configure("Treeview",
                        background="#E1E1E1",
                        foreground="#000000",
                        rowheight=25,
                        fieldbackground="#E1E1E1")
        style.map('Treeview', background=[('selected', '#606060')])


        self.employees_table['show']='headings'
        self.employees_table.heading('id_var',anchor="c",text='الرقم الوظيفي')
        self.employees_table.heading('name_var', text='اسم الموظف')
        self.employees_table.heading('Career_var', text='العنوان الوظيفي')
        self.employees_table.heading('Academic_var', text='التحصيل الدراسي')
        self.employees_table.heading('Date_var', text='تاريخ التعيين')
        self.employees_table.heading('serves_var', text='الخدمة المضافة')
        self.employees_table.heading('Degree_var', text='الدرجة')
        self.employees_table.heading('Stage_var', text='المرحلة')
        self.employees_table.heading('Both_var', text='كتب الشكر')
        self.employees_table.heading('premium_var', text='تاريخ اخر علاوه')
        self.employees_table.heading('upgrading_var', text='تاريخ اخر ترفيع')

        self.employees_table.column('id_var',anchor="c",width=100)
        self.employees_table.column('name_var',anchor="c",width=100)
        self.employees_table.column('Career_var',anchor="c",width=100)
        self.employees_table.column('Academic_var',anchor="c",width=100)
        self.employees_table.column('Date_var',anchor="c",width=100)
        self.employees_table.column('serves_var',anchor="c",width=100)
        self.employees_table.column('Degree_var',anchor="c",width=100)
        self.employees_table.column('Stage_var',anchor="c",width=100)
        self.employees_table.column('Both_var',anchor="c",width=100)
        self.employees_table.column('upgrading_var',anchor="c",width=100)
        self.employees_table.column('premium_var',anchor="c",width=100)
        self.employees_table.bind("<ButtonRelease-1>",self.get_curser)

        self.fetch_all()

    def add_Employees (self):
        if self.id_var.get() == "" or self.name_var.get() == "" or self.Career_var.get() == "" or self.Academic_var.get() == "" or self.Date_var.get() == "" or  self.serves_var.get() == ""or   self.Degree_var.get() == ""or  self.Stage_var.get() == ""or self.upgrading_var.get()=="" or self.premium_var.get()==""or  self.Both_var.get()=="":
            messagebox.showinfo('انتبة', 'توجد حقول فارغة')
        else:
           con = sqlite3.connect('employee.db')
           c = con.cursor()
           c.execute("CREATE TABLE IF NOT EXISTS employees(upgrading_var	TEXT,premium_var TEXT,Both_var INTEGER,Stage_var TEXT,Degree_var TEXT,serves_var	INTEGER,Date_var	TEXT,Academic_var TEXT,Career_var TEXT,name_var TEXT,id_var INTEGER )")
           c.execute("insert into employees values(?,?,?,?,?,?,?,?,?,?,?)"
                  ,(
                      self.upgrading_var.get(),
                      self.premium_var.get(),
                      self.Both_var.get(),
                      self.Stage_var.get(),
                      self.Degree_var.get(),
                      self.serves_var.get(),
                      self.Date_var.get(),
                      self.Academic_var.get(),
                      self.Career_var.get(),
                      self.name_var.get(),
                      self.id_var.get(),
                                 ))
           con.commit()
           messagebox.showinfo('حسناً', 'تمت اضافة موظف')
           self.fetch_all()
           self.clear()
           c.close()
           con.close()
    def fetch_all(self):
        con = sqlite3.connect('employee.db')
        c = con.cursor()
        c.execute('select *from employees')
        rows=c.fetchall()
        if len (rows)!=0:
            self.employees_table.delete(*self.employees_table.get_children())
            for row in rows:
                self.employees_table.insert("",END,value=row)
        con.commit()
        con.close()

    def delmployee(self, target=None):

        if len(self.dele_var.get()) == 0:
            messagebox.showinfo("تحذير!", "يرجى كتابة الاسم المراد حذفه")
        else:
            con = sqlite3.connect('employee.db')
            c = con.cursor()
            query = "DELETE FROM employees WHERE name_var LIKE ?"
            c.execute(query, (self.dele_var.get(),))
            result = tkMessageBox.askquestion('حذف بيانات',
                                          'فعلاً تُريد حذف البيانات', icon="warning")
        if result == 'yes':
         con.commit()
         con.close()
         self.fetch_all()
    def clear(self):
                          self.id_var.set('')
                          self.name_var.set('')
                          self.Career_var.set('')
                          self.Academic_var.set('')
                          self.Date_var.set('')
                          self.serves_var.set('')
                          self.Degree_var.set('')
                          self.Stage_var.set('')
                          self.Both_var.set('')
                          self.premium_var.set('')
                          self.upgrading_var.set('')
    def get_curser(self,ev):
        curser_row = self.employees_table.focus()
        content =self.employees_table.item(curser_row)
        row=content['values']
        self.id_var.set(row[10])
        self.name_var.set(row[9])
        self.Career_var.set(row[8])
        self.Academic_var.set(row[7])
        self.Date_var.set(row[6])
        self.serves_var.set(row[5])
        self.Degree_var.set(row[4])
        self.Stage_var.set(row[3])
        self.Both_var.set(row[2])
        self.premium_var.set(row[1])
        self.upgrading_var.set(row[0])

    def updeat(self):
        if self.id_var.get() == "" or self.name_var.get() == "" or self.Career_var.get() == "" or self.Academic_var.get() == "" or self.Date_var.get() == "" or  self.serves_var.get() == ""or   self.Degree_var.get() == ""or  self.Stage_var.get() == ""or self.upgrading_var.get()=="" or self.premium_var.get()==""or  self.Both_var.get()=="":
            messagebox.showinfo('انتبة', 'لايمكنك تعديل البيانات توجد حقول فارغة')
        else:
             con = sqlite3.connect('employee.db')
             c = con.cursor()
             print("con")
             c.execute("update employees set   upgrading_var=?, premium_var= ?,Both_var=?, Stage_var =?,Degree_var=? , serves_var=?, Date_var=? ,Academic_var =? , Career_var=? ,  name_var=?  WHERE id_var LIKE ? "
                         ,(
                      self.upgrading_var.get(),
                      self.premium_var.get(),
                      self.Both_var.get(),
                      self.Stage_var.get(),
                      self.Degree_var.get(),
                      self.serves_var.get(),
                      self.Date_var.get(),
                      self.Academic_var.get(),
                      self.Career_var.get(),
                      self.name_var.get(),
                      self.id_var.get(),
                                 ))
             con.commit()
             messagebox.showinfo('حسناً', 'تمت تعديل البيانات')

             self.fetch_all()
             self.clear()
             con.close()
    def search(self):
        if len(self.search_var.get()) == 0:
            messagebox.showinfo("تحذير!", "يرجى كتابة الاسم المراد البحث عنه")
        elif self.search_var.get() != "":
            self.employees_table.delete(*self.employees_table.get_children())
            conn = sqlite3.connect("employee.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `employees` WHERE `name_var` LIKE ? OR `id_var` LIKE ?",
                           ('%' + ( self.search_var.get()) + '%', '%' + ( self.search_var.get()) + '%'))
            fetch = cursor.fetchall()
            if len(fetch) == 0:
                messagebox.showinfo("تنبية!","العنصر غير موجود")
            for data in fetch:
                self.employees_table.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
    def coding(self):
        messagebox.showinfo("برمجة وتصميم", "عبدالجبارجليل عجيل "
                                            "واتساب 07804331386")

    def Exit(self):
         result = tkMessageBox.askquestion('الخروج من البرنامج', 'هل تريد الخروج من البرنامج؟', icon="warning")
         if result == 'yes':
            exit()
root = Tk()
ob = Employees(root)
root.mainloop()
