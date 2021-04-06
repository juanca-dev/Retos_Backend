from flask_sqlalchemy import SQLAlchemy
import datetime

#Instanciamos el ORM SQL Alchemy
db = SQLAlchemy()

#Creando el modelo de Tarea
class Task(db.Model):
  __tablename__ = 'tareas'

  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String(70),unique=True)
  descripcion = db.Column(db.String(100))
  fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now)

  def __init__(self,titulo,descripcion):
    self.titulo = titulo
    self.descripcion = descripcion