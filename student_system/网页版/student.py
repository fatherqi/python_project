
from flask import Flask,render_template,request,redirect

app = Flask(__name__,static_url_path='/static')


student = [
    {'name':'张三','语文':89,'数学':98,'英语':97,'total':284},
    {'name':'李四','语文':89,'数学':98,'英语':97,'total':284} 
]

@app.route('/')
def hello_world():
    return 'hello World'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        request.form.get('username')
        request.form.get('password')
        return redirect("/admin")
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html',students=student)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        chinese = request.form.get('语文')
        math = request.form.get('数学')
        english = request.form.get('英语')
        total = int(chinese) + int(math) + int(english)
        student.append({'name':username,'语文':chinese,'数学':math,'英语':english,'total':total})
        return redirect('/admin')
    return render_template('add.html')

@app.route('/delete')
def delete():
    username = request.args.get('name')
    for stu in student:
        if stu['name'] == username:
            student.remove(stu)
    return redirect('/admin')

@app.route('/modify',methods=['GET','POST'])
def modify():
    username = request.args.get('name')
    if request.method == 'POST':
        username = request.form.get('username')
        chinese = request.form.get('语文')
        math = request.form.get('数学')
        english = request.form.get('英语')
        total = int(chinese)+int(math)+int(english)

        for stu in student:
            if stu['name'] == username:
                stu['语文'] = chinese
                stu['数学'] = math
                stu['英语'] = english
                stu['total'] = total
        return redirect('/admin')

    for stu in student:
        if stu['name'] == username:
            return render_template('modify.html',student=stu)

if __name__ == '__main__':
    app.run()