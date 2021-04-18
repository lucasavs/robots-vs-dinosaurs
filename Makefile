run:
	uvicorn app.main:app --reload

lint:
	black . --check
	flake8 .

beautify:
	black .

test:
	python3 -m pytest
