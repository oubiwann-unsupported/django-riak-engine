from django.db.utils import DatabaseError

from djangotoolbox.db import basecompiler

from django_riak_engine import maps
from django_riak_engine.util import decorators


class BackendQuery(basecompiler.NonrelQuery):

    def __init__(self, compiler, fields):
        super(BackendQuery, self).__init__(compiler, fields)
        # TODO: add your initialization code here
        # note that django_mongodb_engine sets self.db_query to a dict
        self.db_query = LowLevelQuery(self.connection.db_connection)

    # This is needed for debugging
    def __repr__(self):
        # TODO: add some meaningful query string for debugging
        return '<BackendQuery: ...>'

    @decorators.safe_call
    def fetch(self):
        # TODO: run your low-level query here
        low_mark, high_mark = self.limits
        if high_mark is None:
            # Infinite fetching
            results = self.db_query.fetch_infinite(offset=low_mark)
        elif high_mark > low_mark:
            # Range fetching
            results = self.db_query.fetch_range(high_mark - low_mark, low_mark)
        else:
            results = ()

        for entity in results:
            entity[self.query.get_meta().pk.column] = entity['_id']
            del entity['_id']
            yield entity

    @decorators.safe_call
    def count(self, limit=None):
        # TODO: implement this
        return self.db_query.count(limit)

    @decorators.safe_call
    def delete(self):
        # TODO: implement this
        self.db_query.delete()

    @decorators.safe_call
    def order_by(self, ordering):
        # TODO: implement this
        for order in ordering:
            if order.startswith('-'):
                column, direction = order[1:], 'DESC'
            else:
                column, direction = order, 'ASC'
            if column == self.query.get_meta().pk.column:
                column = '_id'
            self.db_query.add_ordering(column, direction)

    # This function is used by the default add_filters() implementation which
    # only supports ANDed filter rules and simple negation handling for
    # transforming OR filters to AND filters:
    # NOT (a OR b) => (NOT a) AND (NOT b)
    @decorators.safe_call
    def add_filter(self, column, lookup_type, negated, db_type, value):
        # TODO: implement this or the add_filters() function (see the base
        # class for a sample implementation)

        # Emulated/converted lookups
        if column == self.query.get_meta().pk.column:
            column = '_id'

        if negated:
            try:
                op = maps.NEGATION_MAP[lookup_type]
            except KeyError:
                raise DatabaseError("Lookup type %r can't be negated" % lookup_type)
        else:
            try:
                op = maps.OPERATORS_MAP[lookup_type]
            except KeyError:
                raise DatabaseError("Lookup type %r isn't supported" % lookup_type)

        # Handle special-case lookup types
        if callable(op):
            op, value = op(lookup_type, value)

        db_value = self.convert_value_for_db(db_type, value)
        self.db_query.filter(column, op, db_value)

