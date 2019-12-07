#src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()
#######
# existing code remains #
#######
from .BlogpostModel import BlogpostModel, BlogpostSchema
from .UserModel import UserModel, UserSchema