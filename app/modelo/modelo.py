from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages, abort

from app.modelo.configuracion_bbdd_formulario import Recetario
from app import db, app, mysql
from app.modelo.configuracion_bbdd_formulario import RecetaFormulario, FormSINO
from flask_login import login_required
from flask_login import login_required
from werkzeug.utils import secure_filename

import os
recetas = Blueprint('receta', __name__)


@recetas.before_request
@login_required
def validacion():
    pass

@recetas.route('/')
def inicio():
    recetas = Recetario.query.group_by(Recetario.tipo)
    print(recetas)
    return render_template('/vistas/inicio.html', recetas=recetas)

@recetas.route('/listado/<tipo>')
def listado(tipo):
    tipoReceta = Recetario.query.filter_by(tipo=tipo).all()
    return render_template('/vistas/listado.html', tipo=tipoReceta)

@recetas.route('/recetario')
@recetas.route('/recetario/<int:page>')
def index(page=1):
    recetas=Recetario.query.order_by(Recetario.nombre.asc())
    return render_template('/vistas/index.html', recetas=recetas.paginate(page, 10))

@recetas.route('/receta/<int:id>')
def mostrar(id):
    recetas = Recetario.query.get_or_404(id)
    return render_template('/vistas/receta.html', receta=recetas)

@recetas.route('/receta/nueva', methods=('GET', 'POST'))
@login_required
def nueva():
    formulario = RecetaFormulario(meta={'csrf':False})

    if formulario.validate_on_submit():
        try:
            f = formulario.foto.data
            nombre_fichero = secure_filename(f.filename)
            f.save(app.root_path + "/static/uploads/" + nombre_fichero)
        except:
            nombre_fichero = "sin_imagen.png"
        rec = Recetario(request.form['nombre'], request.form['ingredientes'], request.form['elaboracion'], request.form['tipo'], request.form['observaciones'])
        rec.foto = nombre_fichero
        db.session.add(rec, rec.foto)
        db.session.commit()
        flash("Producto creado con éxito")
        return redirect(url_for('receta.index'))
    else:
        return render_template('/vistas/nueva.html', formularios=formulario)

@recetas.route('/receta/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    receta = Recetario.query.get_or_404(id)
    formulario = RecetaFormulario(meta={'csrf':False})

    if request.method == 'GET':
        formulario.nombre.data = receta.nombre
        formulario.ingredientes.data = receta.ingredientes
        formulario.elaboracion.data = receta.elaboracion
        formulario.tipo.data = receta.tipo
        formulario.observaciones.data = receta.observaciones
        formulario.foto.data = receta.foto


    if formulario.validate_on_submit():
        if formulario.foto.data:
            f = formulario.foto.data
            nombre_fichero = secure_filename(f.filename)
            receta.foto = nombre_fichero
            f.save(app.root_path + "/static/uploads/" + nombre_fichero)
            db.session.add(receta)
            db.session.commit()
            flash("Foto actualizada")
        elif formulario.foto.data is None:
            receta.nombre = formulario.nombre.data
            receta.ingredientes = formulario.ingredientes.data
            receta.elaboracion = formulario.elaboracion.data
            receta.tipo = formulario.tipo.data
            receta.observaciones = formulario.observaciones.data
            db.session.add(receta)
            db.session.commit()
            flash("Receta actualizada")
        return redirect(url_for('receta.mostrar', id=receta.id))



    return render_template('/vistas/editar.html', receta=receta, formularios=formulario)


@recetas.route('/receta/eliminar/<int:id>')
def eliminar(id):
    receta = Recetario.query.get_or_404(id)
    db.session.delete(receta)
    db.session.commit()
    flash("Receta eliminada con éxito")
    return redirect(url_for('receta.index'))
'''
@recetas.route('/receta/eliminar/<int:id>',  methods=['GET', 'POST'])
def eliminar(id):
    receta = Recetario.query.get_or_404(id)
    if receta is None:
        abort(404)
    formulario = FormSINO(meta={'csrf':False})
    if formulario.validate_on_submit():
        if formulario.si.data:
            db.session.delete(receta)
            db.session.commit()
        return redirect(url_for('receta.index'))
    return render_template("/vistas/eliminar.html", formularios=formulario, receta=receta)
'''

@recetas.route('/novedades')
@recetas.route('/novedades/<int:page>')
def novedades(page=1):
    # EJEMPLO DE CONSULTA COMPLEJA
    #    recetas=Recetario.query.filter(Recetario.tipo.like('%Aperitivo%')).order_by(Recetario.nombre.asc()).all()
    #    print (recetas)
    recetas=Recetario.query.order_by(Recetario.id.desc())
    return render_template('/vistas/novedades.html', recetas=recetas.paginate(page, 10))



#EL BUSCADOR NO ESTA HECHO CON SQLALCHEMY YA QUE NO SE COMO PASARLE UNA VARIABLE ES UNA FUNCIÓN f
@recetas.route('/vistas/buscar', methods=['POST'])
def buscar():
    if request.method == 'POST':
        receta = request.form['receta']
        cur = mysql.connection.cursor()
        receta = f"%{receta}%"
        cur.execute("select * from Receta where nombre like %s", {receta})
        receta = cur.fetchall()
        return render_template("/vistas/buscador.html", receta=receta)
