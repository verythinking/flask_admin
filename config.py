#! -*- coding:utf-8 -*-


class Config(object):
    """ 配置类 """
    SECRET_KEY = 'if i dont tell you can you guess'


class DevelopConfig(Config):
    DEBUG = True

    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mahui@127.0.0.1:3306/wuchan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductConfig(Config):
    DEBUG = False
    TESTING = False
