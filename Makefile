PYTHON_BINARY ?= python2.5
VERSION = $(shell $(PYTHON_BINARY) -c \
PYTHONPATH = $$PYTHONPATH

version:
	"from django_riak_engine.meta import version; print version;")

build:
	$(PYTHON_BINARY) setup.py build

check: DJANGO_HOME ?= 
check: build
	$(PYTHON_BINARY) ./django_riak_engine/testing/runner.py
#	cd ./examples/django_riak_mapreduce/ && \
#	PYTHONPATH=$(DJANGO_HOME):../..:$(PYTHONPATH) \
#	$(PYTHON_BINARY) ./manage.py test

install: check
	sudo $(PYTHON_BINARY) setup.py install

push: clean check
	git push

commit-push: clean check
	git commit -v -a
	git push

register:
	$(PYTHON_BINARY) setup.py register

upload-docs: build-docs
	$(PYTHON_BINARY) setup.py upload_docs --upload-dir=docs/html/

release: push
release:
	git tag $(VERSION)
	$(PYTHON_BINARY) setup.py sdist upload --show-response

clean:
	rm -rf build sdist dist *.egg *.egg-info
	find . -name *.pyc -exec rm {} \;

# project-app usage:
#
# make START=~/lab PROJECT=django_riak_example APP=riak_app project-app
project-app: START ?= .
project-app: PROJECT ?= test-project
project-app: APP ?= test-app
project-app: DJANGO_HOME ?= /usr/local/google_appengine/lib/django_1_2
project-app:
	cd $(START) && PYTHONPATH=$(DJANGO_HOME):$(PYTHONPATH) \
	python2.5 $(DJANGO_HOME)/django/bin/django-admin.py \
	startproject $(PROJECT) && \
	cd $(PROJECT) && \
	PYTHONPATH=$(DJANGO_HOME):$(PYTHONPATH) \
	python2.5 $(DJANGO_HOME)/django/bin/django-admin.py \
	startapp $(APP)

load-example-data:
	cd ./examples/django_riak_mapreduce/riak_mapreduce && \
	PYTHONPATH=.:$(PYTHONPATH) \
	python2.6 -c "import tools; tools.import_csv_google_data();"
