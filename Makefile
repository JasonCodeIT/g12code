all: run

run:
	python audit.py

clean:
	rm -rf output/*
