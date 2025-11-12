from flask import Flask, render_template,request,redirect,url_for
from db_config import db
from Mascota import Mascota

class Programa:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///estudiantes.sqlite3"
        # agregar database a nuestra aplicacion
        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscartodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])

        # iniciar el servidor 
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)

    def buscartodos(self):
       return render_template('mostrartodos.html', mascotas=Mascota.query.all())
       
    def agregar(self):

        #VERIFICAR SI DEBE ENVIAR EL FORMULARIO O PROCESAR LOS DATOS
        if request.method=="POST":
         #CREAR UN EJEMPLO DE LA CLASE ESTUDIANTE CON LOS VALORES DEL FORMULARIO 
         nombre=request.form['nombre']
         raza=request.form['raza']
         edad=request.form['edad']
         mimascota=Mascota(nombre,raza,edad)
        #guardar el objeto en la base de datos
         db.session.add(mimascota)
         db.session.commit()

         return redirect( url_for('buscartodos'))

        return render_template('nuevamascota.html')

miprograma = Programa()
