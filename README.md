# Titanic Survival Analysis App

## Overview
This is a Streamlit web application that visualizes the survival rates of passengers from the Titanic disaster. It provides insights into the factors influencing survival, including gender, class, fare, age, and the number of parents/children aboard.

## Features
- **Survival Rates by Gender**: Visualizes the proportion of male and female survivors.
- **Survival Rate by Class**: Shows the average survival rate based on passenger class.
- **Fare Distribution**: Displays the distribution of survivors based on ticket fare.
- **Age Distribution**: Compares the age distribution of survivors and non-survivors.
- **Parch (Parents/Children Aboard) vs Survival**: Visualizes the relationship between the number of parents/children aboard and survival outcomes.

## Technologies Used
- **Python**: The primary programming language.
- **Streamlit**: A web framework for building interactive applications.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **Docker**: For containerizing the application.

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt

4. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py


## Docker Instructions
To containerize the application using Docker:

1. **Build the Docker image**:
   ```bash
   docker build -t titanicapp .

2. **Run the Docker container**:
   ```bash
   docker run -p 8501:8501 titanicapp

3. **Access the app**:
   Open your web browser and go to http://localhost:8501.


