from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin
from flask_restful import Api

# WSGI application object.
app = Flask(__name__)
CORS(app)

# Load configuration.
app.config.from_object('config')

# Database object.
db = MongoEngine(app)

# REST api interface.
api = Api(app)

# Routing
# Import blueprint modules
from app.users.views import UsersView, UserView, LoginView
from app.todos.views import TodosView, TodoView
# Register routes
api.add_resource(UserView, '/user/<string:id>')
api.add_resource(UsersView, '/user')
api.add_resource(LoginView, '/login')
api.add_resource(TodoView, '/todo/<string:id>')
api.add_resource(TodosView, '/todo')
