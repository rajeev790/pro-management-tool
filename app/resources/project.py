from flask_restful import Resource
from flask import request
from app import db
from app.models import Project
from app.schemas.project_schema import project_schema, projects_schema

class ProjectListResource(Resource):
    def get(self):
        projects = Project.query.all()
        return projects_schema.dump(projects)

    def post(self):
        data = request.get_json()
        new_project = Project(
            name=data['name'],
            description=data['description'],
            user_id=data['user_id']
        )
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project)

class ProjectResource(Resource):
    def get(self, id):
        project = Project.query.get_or_404(id)
        return project_schema.dump(project)

    def put(self, id):
        project = Project.query.get_or_404(id)
        data = request.get_json()
        project.name = data['name']
        project.description = data['description']
        project.updated_at = datetime.utcnow()
        db.session.commit()
        return project_schema.dump(project)

    def delete(self, id):
        project = Project.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return '', 204