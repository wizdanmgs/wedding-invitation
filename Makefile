.PHONY: up
up:
	docker compose up

.PHONY: down
down:
	docker compose down

.PHONY: prod-up
prod:
	docker compose -f docker-compose.prod.yml up -d --build
	docker compose exec web python manage.py collectstatic --no-input


.PHONY: prod-down
prod:
	docker compose -f docker-compose.prod.yml down

