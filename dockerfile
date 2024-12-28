# Use an updated base image with Python 3.8
FROM python:3.8-slim-bullseye

# Set up the working directory
WORKDIR /app

# Copy application code
COPY ./main.py .
COPY mylib/ ./mylib/
COPY ./requirements.txt .

# Install necessary dependencies and update OpenSSL
RUN apt-get update && apt-get install -y \
    libssl-dev wget build-essential zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Update OpenSSL manually to ensure compatibility
RUN wget https://www.openssl.org/source/openssl-1.1.1v.tar.gz && \
    tar -xvzf openssl-1.1.1v.tar.gz && \
    cd openssl-1.1.1v && \
    ./config && \
    make && \
    make install && \
    cd .. && \
    rm -rf openssl-1.1.1v*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8080

# Define the command to run the application
ENTRYPOINT ["python", "main.py"]
