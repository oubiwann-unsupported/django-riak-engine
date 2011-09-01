from django_riak_engine import client

from djangotoolbox.db.base import NonrelDatabaseFeatures, \
    NonrelDatabaseOperations, NonrelDatabaseWrapper, \
    NonrelDatabaseValidation, NonrelDatabaseIntrospection, \
    NonrelDatabaseCreation


# TODO: You can either use the type mapping defined in NonrelDatabaseCreation
# or you can override the mapping, here:
class DatabaseCreation(NonrelDatabaseCreation):
    pass


class DatabaseFeatures(NonrelDatabaseFeatures):
    pass


class DatabaseOperations(NonrelDatabaseOperations):
    compiler_module = __name__.rsplit('.', 1)[0] + '.compiler'


class DatabaseValidation(NonrelDatabaseValidation):
    pass


class DatabaseIntrospection(NonrelDatabaseIntrospection):
    pass


class DatabaseWrapper(NonrelDatabaseWrapper):
    def __init__(self, *args, **kwds):
        super(DatabaseWrapper, self).__init__(*args, **kwds)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.client = client.DatabaseClient(self)
        self.creation = DatabaseCreation(self)
        self.validation = DatabaseValidation(self)
        self.introspection = DatabaseIntrospection(self)
        # TODO: connect to your DB here (if needed)
        self.db_connection = connect(
            self.settings_dict['HOST'], self.settings_dict['PORT'],
            self.settings_dict['USER'], self.settings_dict['PASSWORD'])
