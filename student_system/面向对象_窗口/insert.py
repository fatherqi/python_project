#!/usr/bin/env python3
import tkinter
from db import OpenText
import time

class InsertFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        self.root = root
        self.username = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.create_insert_page()
        
    def create_insert_page(self):
       tkinter.Label(self,text='姓名').grid(row=1,column=0,padx=5,pady=5)
       tkinter.Entry(self,textvariable = self.username).grid(row=1,column=1,padx=5,pady=5)
       tkinter.Label(self,text='语文').grid(row=2,column=0,padx=5,pady=5)
       tkinter.Entry(self,textvariable = self.chinese).grid(row=2,column=1,padx=5,pady=5)
       tkinter.Label(self,text='数学').grid(row=3,column=0,padx=5,pady=5)
       tkinter.Entry(self,textvariable = self.math).grid(row=3,column=1,padx=5,pady=5)
       tkinter.Label(self,text='英语').grid(row=4,column=0,padx=5,pady=5)
       tkinter.Entry(self,textvariable = self.english).grid(row=4,column=1,padx=5,pady=5)
       tkinter.Button(self,text='录入',command = self.insert_login).grid(row=5,column=1)

    def insert_login(self):
        username = self.username.get()
        chinese = int(self.chinese.get())
        math = int(self.math.get())
        english = int (self.english.get()) 
        total = chinese + math + english 
        student_score = {'name':username,
                         '语文':chinese,
                         '数学':math,
                         '英语':english,
                         'total':total
                         }
        opera = OpenText()
        opera.insert(student_score)  

        self.next_insert_page()

    def next_insert_page(self):
        lebal_prompt = tkinter.Label(self,text='您已录入成功')
        lebal_prompt.grid(row=6,column=1)
        self.after(1000,lebal_prompt.destroy)


class SearchFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        self.root = root
        self.username = tkinter.StringVar()
        self.create_search_page()

    def create_search_page(self):
        tkinter.Label(self,text='姓名').grid(row=1,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.username).grid(row=1,column=1,padx=5,pady=5)
        tkinter.Button(self,text='查询',command = self.search_login).grid(row=5,column=1)
    
    def search_login(self):
        opera = OpenText()
        subject = opera.subject()
        student_value = opera.search(self.username.get())
        self.next_search_page(student_value,subject)

    def next_search_page(self,student_value,subject):

        search_window = tkinter.Toplevel(self.root)
        search_window.geometry('400x120')
        search_window.title('成绩查询')
        tkinter.Label(search_window, text=f'{subject}').pack() 
        tkinter.Label(search_window, text=f'{student_value}').pack()

class DisplayFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        self.root = root

    def display_page(self):
        display_window = tkinter.Toplevel(self.root)
        display_window.title('全部成绩')
        opera = OpenText()
        subject = opera.subject()
        students = opera.all()
        tkinter.Label(display_window,text=f'{subject}').pack()
        for student in students:
            tkinter.Label(display_window, text='{}\t{}\t{}\t{}\t{}'.format(*student.values())).pack()

class DeleteFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        self.root = root   
        self.username = tkinter.StringVar() 
        self.create_delete_page() 

    def create_delete_page(self):
        tkinter.Label(self,text='姓名').grid(row=1,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.username).grid(row=1,column=1,padx=5,pady=5)
        tkinter.Button(self,text='删除',command = self.delete_login).grid(row=5,column=1)
        
    def delete_login(self):
        opera = OpenText()
        students = opera.all() 
        self.next_delete_page(students)   
        opera.delete(self.username.get())
    
    def next_delete_page(self,students):
        label_text = tkinter.Label(self, text='')
        label_text.grid(row=6, column=1) 
        for student in students:
            if student['name'] == self.username.get(): 
                label_text.config(text="您已删除成功")
                break 
        else:
            label_text.config(text="名字输入有误")

        self.after(1000,label_text.destroy)

class ModifyFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        self.username = tkinter.StringVar()
        self.chinese = tkinter.StringVar()
        self.math = tkinter.StringVar()
        self.english = tkinter.StringVar()
        self.opera = OpenText()
        self.students = self.opera.all() 
        self.create_modify_page()
    
    def create_modify_page(self):
        tkinter.Label(self,text='姓名').grid(row=1,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.username).grid(row=1,column=1,padx=5,pady=5)
        tkinter.Label(self,text='语文').grid(row=2,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.chinese).grid(row=2,column=1,padx=5,pady=5)
        tkinter.Label(self,text='数学').grid(row=3,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.math).grid(row=3,column=1,padx=5,pady=5)
        tkinter.Label(self,text='英语').grid(row=4,column=0,padx=5,pady=5)
        tkinter.Entry(self,textvariable = self.english).grid(row=4,column=1,padx=5,pady=5)
        tkinter.Button(self,text='修改',command = self.modify_login).grid(row=5,column=1) 

    def modify_login(self):
        for student in self.students:
            if student['name'] == self.username.get():
               self.opera.modify(self.username.get(),self.chinese.get(),self.math.get(),self.english.get())  
               label_text = tkinter.Label(self, text='您已修改成功')
               label_text.grid(row=6,column=1,padx=5,pady=5)
               break 
        else:
            label_text = tkinter.Label(self, text='您输入的名字有误')
            label_text.grid(row=6,column=1,padx=5,pady=5)
        self.after(1000,label_text.destroy)    

class AboutFrame(tkinter.Frame):
    def __init__(self,root):
        super().__init__(master = root)
        tkinter.Label(self,text='杨红旗').pack()