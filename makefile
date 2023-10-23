lint:
	isort *.py
	black *.py

run: docker run -p 8000:8000 discordbot

build: docker build -t discordbot . 