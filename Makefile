all: doc bases
doc:
	pdoc wcxf --html --template-dir assets/_pdoc-template --overwrite
bases:
	python3 makebases.py
