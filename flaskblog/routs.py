from flask import render_template ,url_for,flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post


posts = [
    {
        'author': 'ariel cohen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html',posts = posts )

@app.route('/about/')
def about():
    return render_template('about.html',title = 'ABOUT' )

@app.route('/register/',methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # יצירת משתמש חדש לדיבי דרך קלאס יוזר
        user = User(username = form.username.data,password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('your acount created!!!')

        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form=form)

@app.route('/login/',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'ariel' and form.password.data == '33333':
            flash('gooddddd!', 'success')
            return render_template('home.html', posts=posts)
        else:
            flash('baddddd!', 'danger')
    return render_template('login.html',title = 'login',form=form)
