from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, index=True)
    floor = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)
    residents = db.relationship('Resident', backref='room', lazy='dynamic')
    
    def __repr__(self):
        return f'<Room {self.number}>'

class Resident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    birth_date = db.Column(db.Date)
    passport = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    check_in_date = db.Column(db.Date, default=datetime.utcnow)
    check_out_date = db.Column(db.Date)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    payments = db.relationship('Payment', backref='resident', lazy='dynamic')
    
    def __repr__(self):
        return f'<Resident {self.last_name} {self.first_name}>'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    period_start = db.Column(db.Date)
    period_end = db.Column(db.Date)
    status = db.Column(db.String(20), default='оплачено')
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.id'))
    
    def __repr__(self):
        return f'<Payment {self.id} for {self.resident_id}>'
