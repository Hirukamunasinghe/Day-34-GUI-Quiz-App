import requests
paramters ={
    "amount":10,
    "type":"boolean",
    "category":18
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean",params=paramters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

