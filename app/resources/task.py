from flask_restful import Resource
from flask import request
from app import db
from app.models import Task
from app.schemas.task_schema import task_schema, tasks_schema

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return tasks_schema.dump(tasks)

    def post(self):
        data = request.get_json()
        new_task = Task(
            name=data['name'],
            description=data['description'],
            project_id=data['project_id'],
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task)

class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id)
        return task_schema.dump(task)

    def put(self, id):
        task = Task.query.get_or_404(id)
        data = request.get_json()
        task.name = data['name']
        task.description = data['description']
        task.status = data['status']
        task.updated_at = datetime.utcnow()
        db.session.commit()
        return task_schema.dump(task)

    def delete(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return '', 204