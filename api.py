import requests


response = requests.get("http://api.example.com/data")
data = response.json()

# CRUD = CREATE READ UPDATE DELETE = POST GET PUT DEL