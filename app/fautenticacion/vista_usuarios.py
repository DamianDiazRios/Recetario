from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.autenticacion.usuarios_bbdd import Usuario,RegistroForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from app import login_manager
from app import db

fautenticacion = Blueprint('fautenticacion', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)


@fautenticacion.route('/registro', methods=('GET', 'POST'))
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
        return redirect(url_for('fautenticacion.registro'))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('autenticacion/registro.html', formulario=form)

@fautenticacion.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        flash("Ya estás logueado "+current_user.usuario)
        return redirect(url_for('receta.index'))

    form = LoginForm(meta={'csrf':False})
    if form.validate_on_submit():
        usuario=Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usuario and usuario.check_password(form.password.data):
            #Si existe el usuario y el password
            login_user(usuario)
            flash("Bienvenido de nuevo "+current_user.usuario)

            next = request.form['next']
            return redirect(next or url_for('receta.inicio'))
        else:
            flash("Usuario no existe", 'danger')
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('autenticacion/login.html', formulario=form)

@fautenticacion.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('fautenticacion.login'))


@fautenticacion.route('/protegida')
@login_required
def protegida():
    return "Vista protegida"

@fautenticacion.route('/protegido')
@login_required
def protegido():
    return "Vista protegido"
