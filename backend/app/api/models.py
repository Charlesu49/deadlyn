from app import db
import datetime
from app import bcrypt
from app import ma


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True, index=True)
    email = db.Column(db.String(255), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<User - '{}'>".format(self.username)

    @property
    def password(self):
        # to ensure password cannot be accessed
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    # userPassword.encode('utf-8')
    def verify_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


# handle serialization with marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)