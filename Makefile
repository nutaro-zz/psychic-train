.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: migrate
migrate:
	docker exec -i clients_api bash -c "python manage.py migrate"
	docker-compose restart clients_api

.PHONY: createsuperuser
createsuperuser:
	docker exec -it clients_api python manage.py createsuperuser --email admin@example.com --username admin