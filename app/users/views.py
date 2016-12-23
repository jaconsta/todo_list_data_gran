from http import HTTPStatus

from flask import request
from flask_restful import Resource

from .models import User
from .serializers import UserSchema, LoginSchema

TODOS= [{'name': "todo1"}, {'name': "todo2"}]


class UserView(Resource):
    """
    Manage todo's based on their _id.
    """

    def get(self, id):
        """
        Find and return the User item.

        :param id: UUID of the database.
        :return: TODO object
        """
        user = User.objects(pk=id).first()
        return UserSchema().dump(user)


class UsersView(Resource):
    """
    Manage the creation and listing of users.
    """
    def get(self):
        """
        Get all users.
        Not implemented due to access rights.

        :return: (List) Users.
        """
        return {'message': 'Not implemented'}, HTTPStatus.NOT_IMPLEMENTED

    def post(self):
        """
        Create a new user.

        :return: User object.
        """
        user_data, errors = UserSchema().load(request.json)
        if errors:
            return errors
        user_data.hash_password()
        user_data.save()

        return UserSchema().dump(user_data)


class LoginView(Resource):
    """
    Login the user.
    """
    def post(self):
        """
        Authenticate the user.
        Currently return users _id as access_token, though an access_token is required.
        """
        login_data, errors = LoginSchema().load(request.json)
        if errors:
            return errors
        # Find and validate user credentials.
        user = User.objects(email=login_data['email']).first()
        if not user or not user.check_password(login_data['password']):
            return {'error': 'Invalid credentials'}, HTTPStatus.BAD_REQUEST
        return {'token': str(user.pk)}
