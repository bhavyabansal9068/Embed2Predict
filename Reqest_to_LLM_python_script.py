import json
import requests


url = 'https://c4dd-35-245-99-122.ngrok.io/query'


# Create the JSON payload with the query
input_data_for_model = {
    'query': "They are dancing happily"
    }

input_json = json.dumps(input_data_for_model)


response = requests.post(url, data=input_json)


print(response.status_code)
print(response.text)