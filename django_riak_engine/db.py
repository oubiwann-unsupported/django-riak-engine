from django_riak_engine import connection
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
        self.db_connection = None
        self.connect()

    def connect(self):
        if not self.db_connection:
            host = self.settings_dict.get('HOST')  # or const.DEFAULT_HOST
            # XXX need to figure out how we're going to deal with HTTP vs. PB
            port = self.settings_dict.get('PORT')  # or const.DEFAULT_HTTP_PORT
            user = self.settings_dict.get('USER')
            password = self.settings_dict.get('PASSWORD')
            self.db_connection = connection.RiakConnection(
                host, port, user, password)
        if not self.db_connection.is_connected():
            self.db_connection.connect()
        return self.db_connection
