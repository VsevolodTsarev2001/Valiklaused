import json

json_data='{"nimi":"Vsevolod Tsarev","vanus":100,"prillid":false}'
data=json.loads(json_data)
print(data)
print(data["nimi"])
for id_,andmed in enumerate(data):
    print(id_,"-",andmed)

for key, value in data.items():
    print(key,":",value)

data2={"nimi":"Martin Sild","vanus":55, "abielus":True, "lapsed":("Inna","Mati"),"koduloomad":None,"autod":
       [
       {"muudel": "BMW","varv":"sinine","joud":500,"number":"123ABC"},
       {"muudel": "Ford","varv":"must","joud":300,"number":"314DOR"}
        ]
       }
print(json.dumps(data2))
print(json.dumps(data2,indent=2, separators=(".","="),sort_keys=True))
with open("data_file.json","w") as write_file:
    json.dump(data2,write_file)

print("Andmed failist:")
with open("data_file.json","r") as r_file:
    data2=json.load(r_file)


print(data2)

