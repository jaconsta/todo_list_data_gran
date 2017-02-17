from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin

# WSGI application object.
from flask_swagger import swagger

API_PREFIX = '/api/v1'

app = Flask(__name__)
CORS(app)

# Load configuration.
app.config.from_object('config')

# Database object.
db = MongoEngine(app)

# REST api interface.
# Document routes
@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "TODO list API"
    return jsonify(swag)

# Routing
# Import blueprint modules
from app.users.views import UserApiListView, UserApiView, LoginApiView
from app.todos.views import TodoApiListView, TodoApiView
# Register routes
app.add_url_rule(API_PREFIX+'/user/<string:id>', view_func=UserApiView.as_view('user'))
app.add_url_rule(API_PREFIX+'/user', view_func=UserApiListView.as_view('user_list'))
app.add_url_rule(API_PREFIX+'/login', view_func=LoginApiView.as_view('user_login'))
app.add_url_rule(API_PREFIX+'/todo/<string:id>', view_func=TodoApiView.as_view('todo'))
app.add_url_rule(API_PREFIX+'/todo', view_func=TodoApiListView.as_view('todo_list'))



