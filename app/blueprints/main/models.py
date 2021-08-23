from flask_user.decorators import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import app, db
from flask import jsonify, render_template, request, session, redirect



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()


class User_team:
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)   
    player = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Player:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    tm = db.Column(db.String)
    pos = db.Column(db.String)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

