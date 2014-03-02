from peewee import *
from config.config import database as dbconfig


db = MySQLDatabase(dbconfig['database'], user=dbconfig['user'], passwd=dbconfig['password'])


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    title = CharField(max_length=80)