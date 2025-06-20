FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 \
    chromium chromium-driver \
    && apt-get clean

# Set environment variables for Chrome to run headless
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set working directory
WORKDIR /tests

# Copy files into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_suite.py .

# Run tests by default
CMD ["python", "test_suite.py"]
