dep:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

install:
	python3 setup.py install

user-install:
	python3 setup.py install --user

test:
	python3 -m unittest

.PHONY: dep build install user-install test
