FROM python:3.11-slim

# System deps for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files first (for cache)
COPY pyproject.toml uv.lock .python-version ./

# Install deps into /code/.venv
RUN uv sync --locked --no-dev

# IMPORTANT: point PATH to correct venv
ENV PATH="/code/.venv/bin:$PATH"

# Copy application code
COPY ingest_data_parameterized.py .

ENTRYPOINT ["python", "ingest_data_parameterized.py"]
