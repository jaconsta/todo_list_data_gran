# Todo list

A simple web application with python, flask, coffeescript, MongoDB and mongoengine.

* [python](https://www.python.org/)
* [flask](http://flask.pocoo.org/)
* [coffeescript](http://coffeescript.org/)
* [MongoDB](https://www.mongodb.com/)
* [mongoengine](http://mongoengine.org/)

##Purpose of Web Application

In this simple web application, user will be able to manage his to-do list.

#Features of Web Application

Build a web application that has the following functions:

* user will be able to **register** with an e-mail address and password
  * when the user clicks on register button, operation must be done with **ajax**.
  * if it's successful, redirect to **login page**
* user will be able to login on that login page
* when the user logs in, he will see the list of to-do items.
* in this page, the user will be able to click on checkboxes placed near of each item.
  * when this checkbox is clicked, that item will marked as completed. 
  * when this checkbox is clicked, operation must be done with **ajax**.
* there will be a **Add New To-Do** button and when the user clicks on it, he will enter a simple one-line text and that text will be added to to-do list.

## Backend methods

Run with

```sh
python run.py
```

It runs on port 8080

Allowed endpoints:

* '/user/<string:id>' : GET
* '/user' : POST
* '/login' : POST
* '/todo/<string:id>' : GET, PUT
* '/todo' : GET, POST

## Web interface

Requirements

Install gulp and dependencies.

```sh
npm install -g gulp-cli
npm install 
```

Run the testing server.

```sh
gulp server
```

It runs on port 8000
