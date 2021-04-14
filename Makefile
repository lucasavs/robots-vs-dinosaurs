run:
	uvicorn app.main:app --reload

lint:
	black . --check

beautify:
	black .

test:
	@echo "TODO"