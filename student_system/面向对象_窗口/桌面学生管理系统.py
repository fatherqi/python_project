#!/usr/bin/env python3
import tkinter 
from main import MainPage

class LoginPage:
    def __init__(self,root_r):
        self.root = root_r
        self.login_frame = tkinter.Frame(self.root)
        self.login_frame.grid()
        
        self.root.title('学生信息管理系统')
        self.root.geometry('300x120')

        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.create_page()

    def create_page(self):
        
        tkinter.Label(self.login_frame,width = 8).grid(row=0,column=0)
        
        tkinter.Label(self.login_frame,text='账户').grid(row=1,column=0)
        tkinter.Entry(self.login_frame,textvariable = self.username).grid(row=1,column=1)
        
        tkinter.Label(self.login_frame,text='密码').grid(row=2,column=0)
        tkinter.Entry(self.login_frame,textvariable = self.password).grid(row=2,column=1)

        tkinter.Button(self.login_frame,text='登陆',command = self.check_login).grid(row=3,column=0)
        tkinter.Button(self.login_frame,text='退出',command = self.root.quit).grid(row=3,column=1)
        
    def check_login(self):
        print('检查登陆')
        print('用户名:',self.username.get())
        print('密码:',self.password.get())
        if self.username.get() == 'yanghongqi' and self.password.get() == '1996yanghongqi':
            print ('登陆成功')
            self.login_frame.destroy()
            MainPage(self.root)
        else:
            print('登陆失败')

root = tkinter.Tk()
login_page = LoginPage(root)
root.mainloop()




