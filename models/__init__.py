#! -*- coding:utf-8 -*-

from flask_security import SQLAlchemyUserDatastore

from init_db import db
from users import Users
from roles import Roles


datastore = SQLAlchemyUserDatastore(db, Users, Roles)
