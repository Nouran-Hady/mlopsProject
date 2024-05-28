Project Overview

This project demonstrates the use of feature selection and Random Forest classification to improve model performance. The final model is deployed using a Flask API and Docker.

Setup Instructions:

Prerequisites
Python 3.8 or higher
Docker
Flask
PySpark
scikit-learn
pandas
numpy

Installation
Clone the Repository:

git clone [https://github.com/SamaOkasha28/AIS477_project.git](https://github.com/Nouran-Hady/mlopsProject.git)

Install Python Dependencies:
pip install --no-cache-dir -r requirements.txt

Running the Pipeline

run AIS477_Project

API Usage
Run the Flask API:

python server.py

Docker Deployment
Build Docker Image:
docker build -t random-forest-api .

Run Docker Container:
docker run -p 5000:5000 random-forest-api

Project Structure
pipeline.py: Contains the code for data preparation, feature selection, and saving chunks.
train_random_forest.py: Contains the code for training the Random Forest model.
server.py: Contains the Flask API code.
requirements.txt: Lists the Python dependencies.
Dockerfile: Contains the Docker configuration.

and the files are attached

then enter to deploy on kubernates services on Azure
