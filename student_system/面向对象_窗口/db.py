#!/usr/bin/env python3
import json

class OpenText():
    def __init__(self):
        with open('practise/student_system/student.json',mode = 'r') as f:
            text = f.read()
        self.student = json.loads(text)

    def insert(self,student_score):
        self.student.append(
            student_score
        )
        self.record(self.student) 
        print('录入成功')

    def subject(self):
        return('姓名\t语文\t数学\t英语\t总分')
     
    def search(self,name):
        for students in self.student:
            if students['name'] == name:
                print('{}\t{}\t{}\t{}\t{}'.format(*students.values()))
                return('{}\t{}\t{}\t{}\t{}'.format(*students.values())) 
                break 
        else:
            print('您输入的名字有误')

    def delete(self,name):
        for students in self.student:
            if students['name'] == name:
                self.student.remove(students) 
                print('您已删除成功')
                self.record(self.student) 
                break 
        else:
            print('您输入的名字有误')

        

    def modify(self,name,chinese,math,english):
        for students in self.student:
            if students['name'] == name:
               if chinese:
                  students['语文'] = int(chinese) 
               if math:
                  students['数学'] = int(math)
               if english:
                  students['英语'] = int(english)   
               total = students['语文'] + students['数学'] + students['英语']
               students['total'] = total  
               print('您已修改成功')            
               self.record(self.student) 
               break
        else:
            print('您输入的名字有误')  
            
    def all(self):
        return self.student

    def record(self,student):
        with open('practise/student_system/student.json',mode = 'w') as f:
            f.write(json.dumps(student,ensure_ascii = False)) 
 

    

