.PHONY: clean install
clean:
	pip uninstall olfactorydecoder -y
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

install:
	python setup.py install