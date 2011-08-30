def getSize(object):
    """APPROXIMATE memory taken by some Python objects in 
    the current 32-bit CPython implementation.

    Excludes the space used by items in containers; does not
    take into account overhead of memory allocation from the
    operating system, or over-allocation by lists and dicts.

    Copied from:
        http://mail.python.org/pipermail/python-list/2008-January/472683.html
    """
    T = type(obj)
    if T is int:
        kind = "fixed"
        container = False
        size = 4
    elif T is list or T is tuple:
        kind = "variable"
        container = True
        size = 4*len(obj)
    elif T is dict:
        kind = "variable"
        container = True
        size = 144
        if len(obj) > 8:
            size += 12*(len(obj)-8)
    elif T is str:
        kind = "variable"
        container = False
        size = len(obj) + 1
    else:
        raise TypeError("don't know about this kind of object")
    if kind == "fixed":
        overhead = 8
    else: # "variable"
        overhead = 12
    if container:
        garbage_collector = 8
    else:
        garbage_collector = 0
    malloc = 8 # in most cases
    size = size + overhead + garbage_collector + malloc
    # Round to nearest multiple of 8 bytes
    x = size % 8
    if x != 0:
        size += 8-x
        size = (size + 8)
    return size
