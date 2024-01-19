#!/usr/bin/env python3
import json
#---------------------------------------
#欢迎使用学生信息管理系统
#1、新建学生信息
#2、显示全部信息
#3、查询学生信息
#4、删除学生信息
#5、修改学生信息
#0、退出系统
#----------------------------------------
info = '''
******************************
欢迎使用学生信息管理系统
1、新建学生信息
2、显示全部信息
3、查询学生信息
4、删除学生信息
5、修改学生信息
0、退出系统
******************************
'''
print (info)

#student = [
#    {'name':'张三','语文':89,'数学':98,'英语':97,'总分':284},
#    {'name':'李四','语文':89,'数学':98,'英语':97,'总分':284} 
#]
with open('student_system/student.json',mode = 'r') as f:
    text = f.read()

student = json.loads(text)

while True:
    number = int(input ('请输入您想要查询的信息:')) 
    if number == 1:
        print ('新建学生信息')
        name = input ('请输入学生的姓名:')
        chinese = int(input ('请输入学生的语文成绩:'))
        math = int(input ('请输入学生的数学成绩:'))
        english = int(input ('请输入学生的英语成绩:'))
        total = chinese + math + english 
        student.append(
            {'name':name,'语文':chinese,'数学':math,'英语':english,'total':total}
        )
        print('已添加成功')
    elif number == 2:
        print ('显示学生信息')
        print ('姓名\t语文\t数学\t英语\t总分') 
        for students in student:
            print('{}\t{}\t{}\t{}\t{}'.format(*students.values()))
    elif number == 3:
        print ('查询学生信息')
        name = input('请输入学生姓名:')
        for students in student:
            if students['name'] == name:
                print ('姓名\t语文\t数学\t英语\t总分') 
                print('{}\t{}\t{}\t{}\t{}'.format(*students.values()))
                break 
        else:
            print('您输入的名字有误')     

    elif number == 4:
        print ('删除学生信息')
        name = input ('请输入您想删除的学生姓名:')
        for students in student:
            if students['name'] == name:
                student.remove(students) 
                print('您已删除成功')
                break 
        else:
            print('您输入的名字有误')         
    elif number == 5:
        print ('修改学生信息')
        name = input('请输入您想修改的学生名字:')
        for students in student:
            if students['name'] == name:
               chinese = input ('请输入学生的语文成绩:')
               if chinese:
                  students['语文'] = int(chinese) 
                
               math = input ('请输入学生的数学成绩:')
               if math:
                  students['数学'] = int(math)

               english = input ('请输入学生的英语成绩:')
               if english:
                  students['英语'] = int(english)   

               total = students['语文'] + students['数学'] + students['英语']
               
               students['total'] = total  

               print('您已修改成功')            
               break 
        else:
            print('您输入的名字有误')           
    elif number == 0:
        print ('退出系统')
        with open('student.json',mode = 'w') as f:
            f.write(json.dumps(student,ensure_ascii = False))
        break
    else:
        print ('输入的选项错误，请重新输入')



