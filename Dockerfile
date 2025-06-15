# Use official Python slim image
FROM python:3.12-slim

# Install OS-level dependencies required for face_recognition
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-all-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY setup.py ./
COPY wealth_estimator/app ./wealth_estimator/app
COPY wealth_estimator/data ./wealth_estimator/data
COPY requirements/ ./requirements/

# Install Python dependencies (from setup.py or requirements.txt)
RUN pip install --upgrade pip && \
    pip install ./

# Expose FastAPI on port 80
EXPOSE 80

# Run FastAPI app using uvicorn
CMD ["uvicorn", "wealth_estimator.app.main:app", "--host", "0.0.0.0", "--port", "80"]
