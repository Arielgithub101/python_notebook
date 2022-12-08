from datetime import datetime
from flaskblog import db




class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(40),nullable=False)
    posts = db.relationship('Post',backref='auther',lazy=True)

    # פה אמור להיכנס טבלת היוזר עם כל העמודות הנדרשות

    def __repr__(self):
        return f'User{self.username}, {self.password}'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    titel = db.Column(db.String(90),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user_id'),nullable=False)

    # פה אמור להיכנס טבלת החברים\תחביבים עם כל העמודות הנדרשות

    def __repr__(self):
        return f'post{self.titel}, {self.date_posted}'
