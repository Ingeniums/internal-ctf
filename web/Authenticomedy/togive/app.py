import os
from flask import Flask, render_template, request, redirect, session

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("FLASK_ENV") == "development"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
FLAG = os.getenv("FLAG")

db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.admin}')"
    
migrate = Migrate(app, db)


@app.route('/')
def index():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        if user.admin:
            return render_template('index.html', flag=FLAG)
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            session['admin'] = user.admin
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin = request.form.get('admin', False) == 'True'  

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('register.html', error='Username already exists')

        new_user = User(username=username, password=password, admin=admin)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username
        session['admin'] = new_user.admin
        return redirect('/')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')
                    
                    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="0.0.0.0")
