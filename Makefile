dep:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

install:
	python3 setup.py install

user-install:
	python3 setup.py install --user

.PHONY: dep build install user-install
