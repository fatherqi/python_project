#!/usr/bin/env python3
import tkinter
from insert import  InsertFrame,SearchFrame,DeleteFrame,ModifyFrame,AboutFrame,DisplayFrame

class MainPage:
    def __init__(self,root_r):
        self.root = root_r
        self.root.title('学生信息管理系统')
        self.root.geometry('400x300')
        self.insertframe = InsertFrame(self.root)
        self.displayframe = DisplayFrame(self.root)
        self.searchframe = SearchFrame(self.root)
        self.deleteframe = DeleteFrame(self.root)
        self.modifyframe = ModifyFrame(self.root)
        self.aboutframe = AboutFrame(self.root)
        self.create_page()

    def create_page(self):
        menu = tkinter.Menu(self.root)
        file_menu = tkinter.Menu(menu, tearoff=False)
        menu.add_cascade(label='applemeun', menu=file_menu)
        file_menu.add_command(label='录入',command = self.show_insert_frame)
        file_menu.add_command(label='显示',command = self.show_display_frame) 
        file_menu.add_command(label='查询',command = self.show_search_frame)
        file_menu.add_command(label='删除',command = self.show_delete_frame)
        file_menu.add_command(label='修改',command = self.show_modify_frame)
        file_menu.add_command(label='关于',command = self.show_about_frame)
        self.root.config (menu=menu)
    
    def show_insert_frame(self):
        self.searchframe.forget() 
        self.displayframe.forget()
        self.deleteframe.forget()
        self.modifyframe.forget()
        self.aboutframe.forget()
        self.insertframe.pack()

    def show_display_frame(self):
        self.searchframe.forget()
        self.insertframe.forget()
        self.deleteframe.forget()
        self.modifyframe.forget()
        self.aboutframe.forget()
        self.displayframe.display_page()

    def show_search_frame(self):
        self.displayframe.forget()
        self.insertframe.forget()
        self.deleteframe.forget()
        self.modifyframe.forget()
        self.aboutframe.forget()
        self.searchframe.pack()

    def show_delete_frame(self):
        self.searchframe.forget()
        self.displayframe.forget()
        self.insertframe.forget()
        self.modifyframe.forget()
        self.aboutframe.forget()
        self.deleteframe.pack()

    def show_modify_frame(self):
        self.searchframe.forget()
        self.displayframe.forget()
        self.insertframe.forget()
        self.deleteframe.forget()
        self.aboutframe.forget()
        self.modifyframe.pack()

    def show_about_frame(self):
        self.searchframe.forget()
        self.displayframe.forget()
        self.insertframe.forget()
        self.deleteframe.forget()
        self.modifyframe.forget()
        self.aboutframe.pack()

















