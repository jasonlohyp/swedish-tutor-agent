# Use the official Python slim image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container at /app
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (Cloud Run default)
EXPOSE 8080

# Set environment variable PORT to 8080
ENV PORT=8080

# Run the streamlit application
CMD ["python", "-m", "streamlit", "run", "streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true"]
