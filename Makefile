setup:
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

run:
	./venv/bin/python3 -m src

test:
	./venv/bin/pytest tests/
