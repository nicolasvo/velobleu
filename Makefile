up:
	docker compose up -d
down:
	docker compose down
start:
	docker compose start && docker compose exec oyster sh
stop:
	docker compose stop
