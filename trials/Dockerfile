FROM python:3.10-slim

# Install git, curl, and Playwright system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    libnss3 \
    libnspr4 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN pip install --no-cache-dir uv

# Create non-root user
RUN useradd -u 8888 appuser && mkdir -p /app && chown -R appuser /app
WORKDIR /app

# Switch to user
USER appuser

# Pre-install playwright python package & google-genai
RUN uv pip install playwright google-genai
# Install chromium browser binaries
RUN python -m playwright install chromium
