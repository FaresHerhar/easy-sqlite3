setup:
	@./env/bin/pip install -r requirements.txt

run:
	@python src/main.py

.PHONY: setup run
