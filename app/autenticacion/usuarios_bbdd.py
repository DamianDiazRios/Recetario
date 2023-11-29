from app import db

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, HiddenField
from wtforms.validators import InputRequired, EqualTo
from sqlalchemy import Enum
from werkzeug.security import check_password_hash, generate_password_hash

import enum

class   RolUsuario(enum.Enum):
    normal=1
    admin=6

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(255))
    password = db.Column(db.String(300))
    rol = db.Column(Enum(RolUsuario))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, usuario, password, rol = RolUsuario.normal):
        self.usuario = usuario
        self.password = generate_password_hash(password)
        self.rol = rol

    def check_password(self, password):
        return check_password_hash(self.password, password)


#FORMULARIO
class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])
    next = HiddenField('next')

class RegistroForm(FlaskForm):
    usuario = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('confirmar')])
    confirmar = PasswordField('Repite la contraseña')