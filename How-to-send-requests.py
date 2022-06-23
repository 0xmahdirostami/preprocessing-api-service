#how to send Requests
import requests, json

#define Url
api0 = "https://api-service-interpolation.herokuapp.com/"
api1 = "https://api-service-interpolation.herokuapp.com/service1"
localhost = "http://127.0.0.1:80"

#define Data
input1 = open('./input_outputs/service1/input.json', 'r')
input1 = json.load(input1)

#send Request
result=requests.post(url=api1, json=input1)

#convert to Json
result=result.json()

print("\n input: ", input1, "\n  \n output: ", result)