FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    && apt-get clean

# Set environment variables
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set working directory
WORKDIR /tests

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test suite
COPY test_suite.py .

# Run test by default
CMD ["python", "test_suite.py"]
