# Use the official Python image
FROM python:3.11.4-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "streamlit_app.py"]

