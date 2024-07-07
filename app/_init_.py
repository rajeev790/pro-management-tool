from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Initialize Flask app
app = Flask(_name_)
app.config.from_object('config.Config')

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
jwt = JWTManager(app)

# Import and register resources
from app.resources.project import ProjectResource, ProjectListResource
from app.resources.task import TaskResource, TaskListResource
from app.resources.user import UserResource, UserListResource

api.add_resource(ProjectListResource, '/projects')
api.add_resource(ProjectResource, '/projects/<int:id>')
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:id>')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>')