from os import name
from flask import Flask, redirect,render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/details", methods=["GET","POST"])
def details():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        
        if name.isalpha():
           if name.lower() == 'pancras':
              if password == '111':
                  return render_template('page.html' ) 
                  
              else:
                  return render_template('index.html' ,outcome = "Wrong password <br> try again" ) 
              
        else:
            return render_template('index.html' ,outcome = "Username contain only letters " ) 
           
    return render_template("index.html")           
       
if __name__ == "__main__":
    app.run(debug=True)
