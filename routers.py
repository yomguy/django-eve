
class EveRouter(object):
    """
    A router to control all database operations on models in eve
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'eve':
            return 'eve'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'eve':
            return 'eve'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'eve' or \
           obj2._meta.app_label == 'eve:
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'eve':
            return db == 'eve'
        return None
