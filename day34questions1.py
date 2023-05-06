import requests

parameters={
    "amount":10,
    "type":"boolean"
}

response=requests.get("https://opentdb.com/api.php",params=parameters)#get api where we have passed certain
#parameters to make it work
response.raise_for_status()#in case status is 400 something then the code doesnot work then the programme is instantly terminated
ah=response.json()#the json is accessed using this 
print(ah)
print("\n")
print(ah['results'])
question_data=ah['results']#and lastly the result key part is pushed into question_data variable