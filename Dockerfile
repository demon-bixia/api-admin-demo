FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create the app directory
RUN mkdir /app

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
   --mount=type=bind,source=uv.lock,target=uv.lock \
   --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
   uv sync --locked --no-install-project --no-editable

# Copy the project into the intermediate image
COPY . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
   uv sync --locked --no-editable

# Run the application
CMD ["/app/.venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "api_admin_demo.wsgi:application"]
