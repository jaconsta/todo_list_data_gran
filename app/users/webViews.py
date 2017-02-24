from flask import Blueprint, render_template


user_web_blueprint = Blueprint('user_web', __name__)


@user_web_blueprint.route('/')
def user_list_template():
    return render_template('users/user_list.jinja2')


login_web_blueprint = Blueprint('login_web', __name__)


@login_web_blueprint.route('/')
def login_template():
    return render_template('users/login.jinja2')
