from app import ma
from app.models import Project

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        include_fk = True

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)