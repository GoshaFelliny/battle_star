from peewee import *

db = SqliteDatabase('BasePlayer.db')


class BasePlayer(Model):
    "Определение модели игрока в БД"
    name = CharField()
    score = IntegerField()

    class Meta:
        database = db


BasePlayer.create_table()


def add_record(name, score):
    """Добавление игрока в БД"""
    BasePlayer.create(name=name, score=score)

