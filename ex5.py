import json

with open('ex5.json') as json_file:
    ex5 = json.load(json_file)
    ex5[2]['batters']['batter'].append({'id': '1003', 'type': 'Coffee'})
    print(ex5)


with open('ex5.json','w') as json_file:
    json.dump(ex5,json_file)
    