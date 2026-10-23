import json

strPerson = '{"name": "Ali", "languages": ["python", "C#"]}'
dictPerson = json.loads(strPerson)
result = json.dumps(dictPerson, indent = 4, sort_keys = True)

print(strPerson)
print(result)
