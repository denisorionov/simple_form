from app import db


class User(db.Model):
    __table_args__ = {'schema': 'orionov'}

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    middle_name = db.Column(db.String(20), nullable=False)
    bornDate = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=True)


class UserProfiles(db.Model):
    __table_args__ = {'schema': 'orionov'}

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    user = db.relationship('User', backref='user_profiles', uselist=False)
    education = db.Column(db.Text, nullable=True)
    comment = db.Column(db.Text, nullable=True)
    citizenship = db.Column(db.String, nullable=True)
