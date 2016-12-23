import os

# Enable development environment.
DEBUG = True

# Application directory.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database configuration.
MONGODB_SETTINGS = {
    'host': 'mongodb://localhost:27017/todo_list'
}
MONGO_URI = "mongodb://localhost:27017/todo_list"
# MONGO_DBNAME = 'todo_list'
# MONGO_USERNAME = None
# MONGO_PASSWORD = None

# Application threads.
THREADS_PER_PAGE = 2

# CRSF.
CSRF_ENABLED = False
CSRF_SESSION_KEY = "ASecretKey"