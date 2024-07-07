from app import ma
from app.models import Task

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)