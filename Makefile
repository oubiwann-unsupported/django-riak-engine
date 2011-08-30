PYTHON_BINARY ?= python2.5
VERSION = $(shell $(PYTHON_BINARY) -c \
	"from django_riak_engine.meta import version; print version;")

build:
	$(PYTHON_BINARY) setup.py build

check: build
	$(PYTHON_BINARY) ./django_riak_engine/testing/runner.py

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
