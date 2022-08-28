from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, logout_user, current_user
from functools import wraps #Para crear decoradores personalizados
from flask_ckeditor import CKEditor

#pip3 install flask flask-mysqldb
#pip3 install MySQL
#pip3 install flask-login

from flask_mysqldb import MySQL
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['CKEDITOR_SERVER_LOCAL']=True

#Esta parte para implementar el buscador
app.config['MYSQL_HOST']= 'ip_servidor'
app.config['MYSQL_USER']= 'usuario'
app.config['MYSQL_PASSWORD']= 'clave'
app.config['MYSQL_DB']= 'Recetario'
mysql = MySQL(app)
#########################################

app.config.from_object('configuration.ConfiguracionProduccion')
app.config['carga_archivos'] = os.path.realpath('.')
db = SQLAlchemy(app)

#LOGIN_FLASK
login_manager = LoginManager()#Instancia de la clase LoginManager para flask_login
login_manager.init_app(app)#Instacia de app
login_manager.login_view = "fautenticacion.login"
login_manager.login_message = "No tienes permisos"


from app.modelo.modelo import recetas
from app.autenticacion.vista_usuarios import autenticacion
from app.fautenticacion.vista_usuarios import fautenticacion

#VISTAS
app.register_blueprint(recetas)
#app.register_blueprint(autenticacion)
app.register_blueprint(fautenticacion)
db.create_all()

