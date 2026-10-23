import json

with open("person.json") as file:
    data = json.load(file)
    print(type(data))
    print(data)
print()

person_dict = {
    "name": "Ali",
    "languages": ["Python", "C#"]
}

result = json.dumps(person_dict)

print(type(result))
print(result)
print()

with open("person.json", "w") as file:
    json.dump(person_dict, file)
