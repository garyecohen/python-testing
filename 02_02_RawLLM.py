llm_text = '''
{
  "foods": [
    {"name": "chips", "calories": 150}
    ]
}
'''

import json
def parse_and_check(text):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        print("Invalid JSON")
        return
    
    if "foods" not in data:
        print("Missing key: foods")
        return
    
    print ("Foods key exists!")
    print ("Number of food items:", len(data["foods"]))

parse_and_check(llm_text)
