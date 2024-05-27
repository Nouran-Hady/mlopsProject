import requests

url = 'http://localhost:5000/predict'
data = {'features': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]}  # Example feature values

response = requests.post(url, json=data)
print(response.json())
