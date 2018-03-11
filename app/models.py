from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint

from app import db
from app import login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # matches = db.relationship('Match', backref='player', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Match(db.Model):

    __table_args__ = (UniqueConstraint('player_1_id','player_2_id',
                      name = 'unique_oponents'),)

    id = db.Column(db.Integer, primary_key=True)
    player_1_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    player_2_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

    player_1 = relationship("User", foreign_keys=[player_1_id])
    player_2 = relationship("User", foreign_keys=[player_2_id])

    score_1 = db.Column(db.Integer)
    score_2 = db.Column(db.Integer)


    def __repr__(self):
        return f'<Match {self.player_1.id} vs {self.player_2.id}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))