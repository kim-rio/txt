from os import error
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        
        if username == 'user_03' and password == '1234':
            return render_template('page.html')
        else:
            return render_template('home.html',error='Invalid username or passord')
     
    else:
        return render_template('home.html')    
            

if __name__ == '__main__':
    app.run(debug=True)
