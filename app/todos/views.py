from http import HTTPStatus

import jwt
from flask import request, jsonify
from flask.views import MethodView

from app.users.models import User
from .models import Todo
from .serializers import TodoSchema


def forbidden():
    return jsonify({'error': 'Not authenticated.'}), HTTPStatus.FORBIDDEN


class TodoApiView(MethodView):
    def get(self, id):
        jwt_token = request.headers.get('Authorization')
        user_id = jwt.decode(jwt_token, 'secret', algorithms=['HS256']).get('userId')
        if not user_id:
            return forbidden()

        # TODO: Review functionality
        todo = Todo.objects(pk=id, user=user_id).first()
        if not todo:
            return jsonify({'message': 'Todo does not exist or belong to the user.'}), HTTPStatus.BAD_REQUEST
        return jsonify(TodoSchema().dump(todo))

    def put(self, id):
        jwt_token = request.headers.get('Authorization')
        user_id = jwt.decode(jwt_token, 'secret', algorithms=['HS256']).get('userId')
        if not user_id:
            return forbidden()
        # todo_update, errors = TodoSchema().load(request.json)
        # if errors:
        #     return errors
        user = User.objects(pk=user_id).first()
        todo = Todo.objects(pk=id, user=user).first()
        new_todo, errors = TodoSchema().update(todo, request.json)
        if errors:
            return errors, HTTPStatus.BAD_REQUEST
        new_todo.save()

        return TodoSchema().dump(new_todo)


class TodoApiListView(MethodView):
    def get(self):
        jwt_token = request.headers.get('Authorization')
        user_id = jwt.decode(jwt_token, 'secret', algorithms=['HS256']).get('userId')
        if not user_id:
            return forbidden()

        todo_list = Todo.objects(user=user_id)

        return jsonify(TodoSchema().dump(todo_list, many=True))

    def post(self):
        jwt_token = request.headers.get('Authorization')
        user_id = jwt.decode(jwt_token, 'secret', algorithms=['HS256']).get('userId')
        if not user_id:
            return forbidden()
        user = User.objects(pk=user_id).first()
        todo_data, errors = TodoSchema().load(request.json)
        if errors:
            return errors
        todo_data.set_user(user)
        todo_data.save()
        return jsonify(TodoSchema().dump(todo_data))
