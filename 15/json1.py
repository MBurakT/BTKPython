import json

person = {
    "name": "Ali",
    "languages": ["python", "C#"]
}

result = person["name"]
result = person["languages"][0]

strPerson = '{"name": "Ali", "languages": ["python", "C#"]}'

result = json.loads(strPerson) # JSON to dict

result = result["name"]

print(result)
