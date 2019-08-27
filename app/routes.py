from app import app
from flask import Flask, render_template, redirect, flash
from flask import request

from app.forms import LoginForm, RegisterForm

from flask_sqlalchemy import SQLAlchemy
#from app.models import PersonData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PersonData.sqlite3'
app.config['SECRET_KEY'] = 'you-will-never-guess'

db =SQLAlchemy(app)


class PersonData(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    name = db.Column(db.String(20))
    email = db.Column(db.String(50))

def __init__(self, username, password, name, email):
    self.username = username
    self.password = password
    self.name = name
    self.email = email


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Log In', form=form)



@app.route('/register', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    #if request.method =='POST':
        #if form.validate_on_submit():
            #try:
                #new_user = PersonsData(form.username.data,form.password.data, form.name.data, form.email.data,  )
                #new_user.authenticated = True
                #session.add(new_user)
                #session.commit()
                #flash('Thanks for registrering')
                #return redirect('/login')
            #except IntegrityError:
                #session.rollback()
                #flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
        #return redirect('/register')
    #return render_template('register.html', titles='Register', form = form)
    if request.method == 'POST':
        if not form['username'] or not form['password'] or not request.form['name'] or not form['email']:
            flash('Please enter all the fields', 'error')
        else:
            persondata = PersonData(form['username'], request.form['password'],
            request.form['name'], request.form['email'])
         
            db.session.add(persondata)
            db.session.commit()
            flash('Record was successfully added')
            return redirect('/login')
    return render_template('register.html', titles = 'Register', form = form)



@app.route('/search')
def search():
    return render_template('search.html', title='Search')




if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)