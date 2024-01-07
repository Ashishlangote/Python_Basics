import json

letters = {'first': 'hello', 'second': 'world'}

with open("index.json", "w") as f:
    json.dump(letters, f)

with open("index.json", "r") as f:
    data = json.load(f)

print(data["first"])
print(type(data))
