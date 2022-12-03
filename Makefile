setup:
	@./env/bin/pip install -r requirements.txt

run:
	@python src/main.py

test:
	@python src/test.py

.PHONY: setup run
