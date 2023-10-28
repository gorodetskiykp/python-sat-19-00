import json

data = {
    'name': "Tom",
    'age': 41,
    "city": "KHB",
    "children": [
        {
            "name": "Глеб",
            "age": 12,
        },
        {
            "name": "Leo",
            "age": 4,
        },
    ]
}

print(data["children"][1]["age"])


with open('bio.json', 'w', encoding='utf8') as f:
    # f.write(str(data))
    f.write(json.dumps(data, indent=2, ensure_ascii=False))

with open('bio.json', 'r') as f:
    new_data = json.loads(f.read())

print(type(new_data))
print(new_data["children"][1]["age"])
