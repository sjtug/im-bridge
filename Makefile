dep:
	pip3 install -r requirements.txt

build:
	python3 setup.py build

.PHONY: dep build
