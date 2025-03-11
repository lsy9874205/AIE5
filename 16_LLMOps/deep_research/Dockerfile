# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies including build tools
RUN apt-get update && apt-get install -y \
    git \
    make \
    gcc \
    g++ \
    pkg-config \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and other project files
COPY . /app/

# Install uv
RUN pip install uv

# Install project dependencies using pyproject.toml
RUN uv pip install --system ".[dev]"

# Expose the port LangGraph runs on
EXPOSE 8000

# Start LangGraph development server
CMD ["uvx", "--refresh", "--from", "langgraph-cli[inmem]", "--with-editable", ".", "--python", "3.11", "langgraph", "dev"]