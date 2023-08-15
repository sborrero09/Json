import json

with open("datos.txt",) as file:
    data = file.readlines()

dic = {"Vendedores":[]}
for d in data[1:]:
    temp = d.replace("/n", "").split(", ")
    dic["Vendedores"].append({
        "Apellido":temp[0],
        "ID":temp[1],
        "Ventas":[int(t) for t in temp[2:]]
    })

with open("DatosFinal.json", "w") as file:
    json.dump(dic, file, indent = 4)    
print(dic)