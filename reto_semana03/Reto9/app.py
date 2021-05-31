from flask import Flask,request,jsonify
from flask_cors import CORS

# Importando modelos y SqlAlchemy
from models import db
from models import Task

# Importando esquemas y marshmallow
from schemas import ma
from schemas import task_schema
from schemas import tasks_schema

#Instanciamos Flask
app = Flask(__name__)
#Configurando CORS
CORS(app)

#Configuración de la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/repasoflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Ruta para obtener y agregar tareas
@app.route('/api/tasks',methods=['GET','POST'])
def manage_tasks():
  if request.method == 'POST':
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    nueva_tarea = Task(titulo,descripcion)
    db.session.add(nueva_tarea)
    db.session.commit()
    return task_schema.jsonify(nueva_tarea)
  elif request.method == 'GET':
    todas_las_tareas = Task.query.all()
    result = tasks_schema.dump(todas_las_tareas)
    return jsonify(result)

@app.route('/api/tasks/<id>',methods=['GET','DELETE','PUT'])
def manage_task(id):
  if request.method == 'GET':
    tarea = Task.query.get(id)
    return task_schema.jsonify(tarea)
  elif request.method == 'PUT':
    tarea = Task.query.get(id)
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    tarea.titulo = titulo
    tarea.descripcion = descripcion
    db.session.commit()
    return task_schema.jsonify(tarea)
  elif request.method == 'DELETE':
    tarea = Task.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    return task_schema.jsonify(tarea)

#Levantando el servidor
if __name__ == '__main__':
  #Relacionando SQLAlchemy y Marshmallow con la App
  db.init_app(app)
  ma.init_app(app)
  #Sincronizando la Base de datos con la App
  with app.app_context():
    #Creando las tablas
    db.create_all()
  app.run(port=5000,debug=True)