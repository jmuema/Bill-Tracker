from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Bill(db.Model):
  '''
  Class that defines bill objects
  '''
  __tablename__ = 'Bills'

  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  bill = db.Column(db.String(255))
  writer = db.Column(db.String(255))
  category = db.Column(db.String(255))
  added_date = db.Column(db.DateTime,default=datetime.utcnow)
  biller = db.Column(db.Integer,db.ForeignKey('users.id'))  

  def __repr__(self):
    return f'Bill{self.bill}'

class User(UserMixin,db.Model):
  '''
  Defining users objects
  '''
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username =  db.Column(db.String(255),index = True)
  email =  db.Column(db.String(255),unique = True,index=True)
  bio = db.Column(db.String(255))
  profile_pic_path  = db.Column(db.String())
  password_secure = db.Column(db.String(255))
  track =  db.relationship('Bill',backref = 'user',lazy='dynamic')
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.password_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_secure,password)

  def __repr__(self):
    return f'User {self.username}'

# class Comment(db.Model):
#   '''
#   Comments data
#   '''
#   __tablename__ = 'comments'

#   id = db.Column(db.Integer,primary_key=True)
#   comment = db.Column(db.String(255))
#   topic = db.Column(db.Integer,db.ForeignKey('blogs.id'))
#   blogger = db.Column(db.Integer,db.ForeignKey('users.id'))

#   def comment_save(self):
#     db.session.add(self)
#     db.session.commit()

#   def delete_comment(self):
#     db.session.delete(self)
#     db.session.commit()

#   def __repr__(self):
#     return f'{self.comment}'