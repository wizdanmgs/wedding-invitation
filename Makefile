.PHONY: dev
dev:
	docker compose up

.PHONY: build
build:
	docker compose -f docker-compose.prod.yml up -d --build
	docker compose exec web python manage.py collectstatic --no-input