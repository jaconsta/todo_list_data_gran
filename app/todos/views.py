from http import HTTPStatus

from flask import request
from flask_restful import Resource

from app.users.models import User
from .models import Todo
from .serializers import TodoSchema


def forbidden():
    return {'error': 'Not authenticated.'}, HTTPStatus.FORBIDDEN


class TodoView(Resource):
    def get(self, id):
        user_id = request.args.get('user')
        if not user_id:
            return forbidden()

        todo = Todo.objects(pk=id, user=user_id).first()

        return TodoSchema().dump(todo)

    def put(self, id):
        user_id = request.args.get('user')
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


class TodosView(Resource):
    def get(self):
        user_id = request.args.get('user')
        if not user_id:
            return forbidden()

        todo_list = Todo.objects(user=user_id)

        return TodoSchema().dump(todo_list, many=True)

    def post(self):
        user_id = request.args.get('user')
        if not user_id:
            return forbidden()
        user = User.objects(pk=user_id).first()
        todo_data, errors = TodoSchema().load(request.json)
        if errors:
            return errors
        todo_data.set_user(user)
        todo_data.save()
        return TodoSchema().dump(todo_data)
