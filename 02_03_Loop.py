import json

llm_text = '''{
    "foods": [
        {"name": "apple", "calories": 92},
        {"name": "pizza"},
        {"name": "banana", "calories": 102}
    ]
}
'''

llm_output = json.loads(llm_text)

if "foods" not in llm_output:
    raise ValueError("Missing required key: foods")

for food in llm_output["foods"]:
    if "calories" in food:
        print(food["name"], "is valid, calories = ", food["calories"])
    else:
        print(food["name"], "is missing calories, skipping for now")