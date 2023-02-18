import json
import os

json_file = os.path.join(os.getcwd(), "sample-data.json")

with open(r"D:\For myself\Edu\python codes\LAB 4\json\sample-data.json") as file:
    data = json.load(file)

print("Interface Status" )
print("="*85)
print("DN                                                 Description           Speed    MTU")
print("-"*50 + " " + "-"*21 + " " + "-"*5 + " " + "-"*6) 
for i in data['imdata']:
    print("{}                             {}  {}".format(i['l1PhysIf']['attributes']['dn'],i['l1PhysIf']['attributes']['fecMode'],i['l1PhysIf']['attributes']['mtu'])) 
        

         