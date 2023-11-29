from app import db

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from flask_wtf.file import FileField
from wtforms.validators import InputRequired
from flask_ckeditor import CKEditorField

class Recetario(db.Model):
    __tablename__='Receta'
    __table_args__ = {'extend_existing' : True}
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    ingredientes = db.Column(db.String(3000))
    elaboracion = db.Column(db.String(3000))
    tipo = db.Column(db.String(20))
    observaciones = db.Column(db.String(255))
    foto = db.Column(db.String(255))
    foto_tipo = db.Column(db.String(255))



    def __init__(self, nombre=None, ingredientes=None, elaboracion=None, tipo=None, observaciones=None, foto=None, foto_tipo=None):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.elaboracion = elaboracion
        self.tipo = tipo
        self.observaciones = observaciones
        self.foto = foto
        self.foto_tipo = foto_tipo


    def __repr__(self):
        return '<Receta %r>' % (self.nombre)


#CLASES PARA EL FORMULARIO
class RecetaFormulario(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired()])
    ingredientes = CKEditorField('Ingredientes', validators=[InputRequired()])
    elaboracion = CKEditorField('Elaboración', validators=[InputRequired()])
    tipo = SelectField('Tipo', choices=[("Carne", "Carne"), ("Pescado", "Pescado"),("Ensaladas", "Ensaladas"), ("Pasta", "Pasta"), ("Guisos", "Guisos"), ("Arroces", "Arroces"), ("Postres", "Postres"), ("Aperitivos", "Aperitivos"), ("Verduras", "Verduras"), ("Pan y Bizcochos", "Pan y Bizcochos"), 
    ("Mambo Guisos", "Mambo Guisos"), ("Mambo Pescado","Mambo Pescado"), ("Mambo Arroces","Mambo Arroces"), ("Mambo Carne","Mambo Carne"), ("Mambo Verdura","Mambo Verdura"), ("Mambo Guisos","Mambo Guisos"), ("Mambo Salsas","Mambo Salsas"), ("Mambo Entrantes", "Mambo Entrantes"), 
    ("Freidora Carne", "Freidora Carne"), ("Freidora Arroces y Patas", "Freidora Arroces y Pastas"), ("Freidora Entrantes", "Freidora Entrantes"), ("Freidora Guarniciones", "Freidora Guarniciones"), ("Freidora Huevos", "Freidora Huevos"), ("Freidora Infantil", "Freidora Infantil"), ("Freidora Masa, Panes y Bollería", "Freidora Masa, Panes y Bollería"), ("Freidora Pescado y Mariscos", "Freidora Pescado y Mariscos"), ("Freidora Postres y Dulces", "Freidora Postres y Dulces"), ("Freidora Sin Gluten", "Freidora Sin Gluten"), ("Freidora Vegetarianas y Veganas", "Freidora Vegetarianas y Veganas"), ("Freidora Verduras y Hortalizas", "Freidora Verduras y Hortalizas")], validators=[InputRequired()])
    observaciones = TextAreaField('Observaciones: ')
    foto = FileField('Selecciona una imagen: ')



class FormSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')
