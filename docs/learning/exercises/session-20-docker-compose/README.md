# Session 20 — Docker & Docker Compose Exercise

## Goal

Run a small production-oriented backend stack:

```
Client
  ↓
FastAPI
  ↓
Docker Compose
  ├── PostgreSQL
  └── Redis
```

The exercise demonstrates:

- Dockerfile
- Docker image/container
- Compose networking
- PostgreSQL named volume
- Redis
- environment variables
- service health checks
- `depends_on` with health conditions
- FastAPI health/readiness endpoints
- container-to-container DNS

## Project structure

```text
session-20-docker-compose/
├── app/
│   └── main.py
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Run

```bash
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f api
```

Then:

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/ready
```

Expected readiness response:

```json
{
  "status": "ready",
  "postgres": "ok",
  "redis": "ok"
}
```

Stop the stack:

```bash
docker compose down
```

Stop it and delete the PostgreSQL volume:

```bash
docker compose down -v
```

> `down -v` deletes the named database volume and therefore the persisted PostgreSQL data.

## Important networking rule

From the host machine:

```text
localhost:8000
```

From inside the `api` container:

```text
postgres:5432
redis:6379
```

Do **not** use `localhost` from the API container to reach PostgreSQL or Redis. Inside a container, `localhost` means that same container.

Compose creates an internal network and provides DNS records using service names.

## Production considerations

This exercise is intentionally small. A production deployment should additionally consider:

- secrets from a secret manager rather than hard-coded Compose values
- pinned image versions/digests
- non-root application user
- resource limits
- database migrations with Alembic
- structured logging
- graceful shutdown
- external monitoring
- backup/restore strategy for PostgreSQL
- TLS and network boundaries
- separate production configuration
- CI image scanning and dependency scanning
