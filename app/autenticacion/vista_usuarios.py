from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.autenticacion.usuarios_bbdd import Usuario,RegistroForm, LoginForm

from app import db

autenticacion = Blueprint('autenticacion', __name__)


@autenticacion.route('/registro', methods=('GET', 'POST'))
def registro():

    if session.get('usuario'):
#    if 'usuario' in session:
        print(session['username'])
    form = RegistroForm(meta={'csrf':False})
    if form.validate_on_submit():
        usua = Usuario(form.usuario.data, form.password.data)
        db.session.add(usua)
        db.session.commit()
        flash("Usuario creado con éxito")
        return redirect(url_for('autenticacion.registro'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('autenticacion/registro.html', formulario=form)

@autenticacion.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(meta={'csrf':False})

    if form.validate_on_submit():
        usuario=Usuario.query.filter_by(usuario=form.usuario.data).first()
        password=usuario.check_password(form.password.data)
        print(form.usuario.data)
        print(form.password.data)
        if usuario and password:
            #Si existe el usuario y el password
            session['usuario'] = usuario.usuario
            session['rol'] = usuario.rol.value
            session['id'] = usuario.id
            flash("Bienvenido de nuevo "+usuario.usuario)
            return redirect(url_for('receta.index'))
        else:
            flash("Usuario no existe", 'danger')
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('autenticacion/login.html', formulario=form)

@autenticacion.route('/logout')
def logout():
    if 'usuario' in session:
        flash("Hasta pronto "+session['usuario'])
        session.pop('usuario')
        session.pop('rol')
        session.pop('id')

        return redirect(url_for('autenticacion.login'))
    else:
        return redirect(url_for('autenticacion.login'))
