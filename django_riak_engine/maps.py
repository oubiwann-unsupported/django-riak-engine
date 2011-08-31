# TODO: Change this to match your DB
# Valid query types (a dictionary is used for speedy lookups).
OPERATORS_MAP = {
    'exact': '=',
    'gt': '>',
    'gte': '>=',
    'lt': '<',
    'lte': '<=',
    'in': 'IN',
    'isnull': lambda lookup_type, value: ('=' if value else '!=', None),

    #'startswith': lambda lookup_type, value: ...,
    #'range': lambda lookup_type, value: ...,
    #'year': lambda lookup_type, value: ...,
}


NEGATION_MAP = {
    'exact': '!=',
    'gt': '<=',
    'gte': '<',
    'lt': '>=',
    'lte': '>',
    'in': 'NOTIN',
    'isnull': lambda lookup_type, value: ('!=' if value else '=', None),

    #'startswith': lambda lookup_type, value: ...,
    #'range': lambda lookup_type, value: ...,
    #'year': lambda lookup_type, value: ...,
}
