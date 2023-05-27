# FastAPI_app
Features:
1) Completely async (exclude migrations, cause they don't to be async at all)
2) Caching with Redis
3) Background processing with Celery (Flower for tasks monitoring)
4) Mailing background task (SMTP). (Ensure you write a real email when registering user!)
5) Chatting module with FastAPI async websockets
6) SQLAlchemy ORM and Alembic migrations
7) Jinja2 templates
8) Dockerized

Installation:
1) Install Docker
2) Copy repository
3) Run [docker compose up --build]

PS: all containers are running on default ports: 
      FastAPI: 8000
      Redis: 6379
      Postgres: 5432
      Flower: 5555
