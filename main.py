from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import session, Base, engine
from models import Users

app = Flask(__name__)

Base.metadata.bind = engine
Base.metadata.create_all(engine)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        error = None
        fuser = request.form['username']
        fpassword = request.form['password']
        account = session.query(Users).filter(Users.username==fuser).first()
        
        if not account or account.password != fpassword :
                error = 'invalid credentials'
                return render_template('login.html', error=error)
        else:
                return render_template('user.html', user = account.username)
    else:
         return render_template('login.html')
    
        
@app.route('/new_user',methods = ['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        user = Users(email = request.form['email'],username = request.form['username'], password = request.form['password'])
        session.add(user)
        session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('registration.html')
    
@app.route('/logout')
def logout():
    if session:
          session.delete()
          return redirect(url_for('login'))
    return redirect(url_for('login'))    


if __name__ == "__main__":
    app.run(debug=True)