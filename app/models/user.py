from app.extensions import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  firebase_uid = db.Column(db.String(255), unique=True, nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  name = db.Column(db.String(255))