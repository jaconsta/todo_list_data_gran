from marshmallow_mongoengine import ModelSchema

from .models import User


class UserSchema(ModelSchema):
    """
    User schema interface.
    """
    class Meta:
        model = User
        model_fields_kwargs = {'password': {'load_only': True}}


class LoginSchema(ModelSchema):
    """
    Fields allowed for login flow.
    """
    class Meta:
        model = User
        fields = ('email', 'password')
