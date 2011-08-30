import os


rest_error_help = """
ReST validation error

See the following:
  http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt
  http://docutils.sourceforge.net/docs/user/rst/quickstart.html
"""

legalReSTFiles = [
    "README",
    "TODO",
    "DEPENDENCIES",
    ]


def setup(*args, **kwds):
    """
    Compatibility wrapper.
    """
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup
    return setup(*args, **kwds)


def find_packages(library_name):
    """
    Compatibility wrapper.

    Taken from storm setup.py.
    """
    try:
        from setuptools import find_packages
        return find_packages()
    except ImportError:
        pass
    packages = []
    for directory, subdirectories, files in os.walk(library_name):
        if "__init__.py" in files:
            packages.append(directory.replace(os.sep, "."))
    return packages


def has_docutils():
    """
    Check to see if docutils is installed.
    """
    try:
        import docutils
        return True
    except ImportError:
        return False


def _validate_ReST(text):
    """
    Make sure that the given ReST text is valid.

    Taken from Zope Corp's zc.twist setup.py.
    """
    import docutils.utils
    import docutils.parsers.rst
    import StringIO

    doc = docutils.utils.new_document("validator")
    # our desired settings
    doc.reporter.halt_level = 5
    doc.reporter.report_level = 1
    stream = doc.reporter.stream = StringIO.StringIO()
    # docutils buglets (?)
    doc.settings.tab_width = 2
    doc.settings.pep_references = doc.settings.rfc_references = False
    doc.settings.trim_footnote_reference_space = None
    # and we're off...
    parser = docutils.parsers.rst.Parser()
    try:
        parser.parse(text, doc)
    except Exception, err:
        import pdb;pdb.set_trace()
    return stream.getvalue()


def validate_ReST(text):
    """
    A wrapper that ensafens the validation for pythons that are not embiggened
    with docutils.
    """
    if has_docutils():
        return _validate_ReST(text)
    print " *** No docutils; can't validate ReST."
    return ""


def cat_ReST(*args, **kwds):
    """
    Concatenate the contents of one or more ReST files.

    Taken from Zope Corp's zc.twist setup.py.
    """
    # note: distutils explicitly disallows unicode for setup values :-/
    # http://docs.python.org/dist/meta-data.html
    tmp = []
    for arg in args:
        if arg in legalReSTFiles or arg.endswith(".rst"):
            f = open(os.path.join(*arg.split("/")))
            tmp.append(f.read())
            f.close()
            tmp.append("\n\n")
        else:
            print "Warning: '%s' not a legal ReST file." % arg
            tmp.append(arg)
    if len(tmp) == 1:
        res = tmp[0]
    else:
        res = "".join(tmp)
    out = kwds.get("out")
    stop_on_errors = kwds.get("stop_on_errors")
    if out is True:
        filename = kwds.get("filename")
        f = open(filename, "w")
        f.write(res)
        f.close()
        report = validate_ReST(res)
        if report:
            print report
            if stop_on_errors:
                print rest_error_help
                raise ValueError("ReST validation error")
    return res
