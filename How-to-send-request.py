#How to send requests
import requests, json

#define Url
api0 = "https://api-service-interpolation.herokuapp.com/"
api1 = "https://api-service-interpolation.herokuapp.com/service1"

#define Data
input1 = open('./input_outputs/service1/input.json', 'r')
input1 = json.load(input1)

#send request
result=requests.post(url=api1, json=input1)

#Convert to json
result=result.json()

print("\n input: ", input1, "\n  \n output: ", result)