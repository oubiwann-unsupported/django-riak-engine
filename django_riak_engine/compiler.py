from djangotoolbox.db.basecompiler import (
    NonrelCompiler, NonrelInsertCompiler, NonrelUpdateCompiler,
    NonrelDeleteCompiler)

from django_riak_engine import query
from django_riak_engine.util import decorators


class SQLCompiler(NonrelCompiler):

    query_class = query.BackendQuery

    # This gets called for each field type when you fetch() an entity.
    # db_type is the string that you used in the DatabaseCreation mapping
    def convert_value_from_db(self, db_type, value):
        # TODO: implement this

        # Handle list types
        if (isinstance(value, (list, tuple)) 
            and len(value) 
            and db_type.startswith('ListField:')):
            db_sub_type = db_type.split(':', 1)[1]
            value = [self.convert_value_from_db(db_sub_type, subvalue)
                     for subvalue in value]
        elif isinstance(value, str):
            # Always retrieve strings as unicode
            value = value.decode('utf-8')
        return value

    # This gets called for each field type when you insert() an entity.
    # db_type is the string that you used in the DatabaseCreation mapping
    def convert_value_for_db(self, db_type, value):
        # TODO: implement this

        if isinstance(value, unicode):
            value = unicode(value)
        elif isinstance(value, str):
            # Always store strings as unicode
            value = value.decode('utf-8')
        elif isinstance(value, (list, tuple)) and len(value) and \
                db_type.startswith('ListField:'):
            db_sub_type = db_type.split(':', 1)[1]
            value = [self.convert_value_for_db(db_sub_type, subvalue)
                     for subvalue in value]
        return value


# This handles both inserts and updates of individual entities
class SQLInsertCompiler(NonrelInsertCompiler, SQLCompiler):

    @decorators.safe_call
    def insert(self, data, return_id=False):
        # TODO: implement this
        pk_column = self.query.get_meta().pk.column
        if pk_column in data:
            data['_id'] = data[pk_column]
            del data[pk_column]
        # XXX use save from database connection
        pk = save_entity(self.connection.db_connection,
            self.query.get_meta().db_table, data)
        return pk


class SQLUpdateCompiler(NonrelUpdateCompiler, SQLCompiler):
    pass


class SQLDeleteCompiler(NonrelDeleteCompiler, SQLCompiler):
    pass
