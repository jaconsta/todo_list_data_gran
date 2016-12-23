from marshmallow_mongoengine import ModelSchema

from .models import Todo


class TodoSchema(ModelSchema):
    class Meta:
        model = Todo

