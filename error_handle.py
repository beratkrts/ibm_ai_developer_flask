    
import requests

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
myobj = { "raw_document": { "text": ""} }

# Make a POST request to the API with the first payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the first response
print(response.status_code)

# Define the second payload with a meaningful text to test the API
myobj = { "raw_document": { "text": "Testing this application for error handling" } }

# Make a POST request to the API with the second payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the second response
print(response.status_code)
 