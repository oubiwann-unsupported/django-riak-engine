from django_riak_engine import meta
from django_riak_engine.util import dist


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: OS Independent',
    ]


for versions in ['2', '2.4', '2.5', '2.6', '2.7']:
    CLASSIFIERS.append('Programming Language :: Python :: %s' % versions)


dist.setup(
    name=meta.name,
    version=meta.version,
    author=meta.author,
    author_email=meta.author_email,
    url=meta.url,
    license=meta.license,
    description=meta.description,
    long_description=dist.cat_ReST(
        "docs/PRELUDE.rst",
        "docs/INTRO.rst",
        "docs/INSTALL.rst",
        "docs/USAGE.rst",
        "TODO",
        "docs/HISTORY.rst",
        stop_on_errors=True,
        out=True,
        filename="README.rst"),

    platforms=['any'],
    install_requires=['riak', 'django>=1.2', 'djangotoolbox'],
    packages=dist.find_packages(meta.library_name),

    classifiers=CLASSIFIERS,
    test_suite='django_riak_engine.tests',
    )
