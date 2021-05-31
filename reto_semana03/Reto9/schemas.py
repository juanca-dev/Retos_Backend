from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TaskSchema(ma.Schema):
  class Meta:
    fields = ('id','titulo','descripcion','fecha_creacion')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)