import json

data = {}
data['cliente'] = []

data['cliente'].append({
                    "cliente":[
                                    {
                                        "Id":	"131544",
                                        "Nombre":	"Felipe Perez",
                                        "NumCuenta":	"32325658",
                                        "Saldo":	1000000
                                    },
                                    {
                                        "Id":	"131222",
                                        "Nombre":	"Juana de Arco",
                                        "NumCuenta":	"487856",
                                        "Saldo":	35000000
                                    },
                                    {
                                        "Id":	"131987",
                                        "Nombre":	"Andres Perez",
                                        "NumCuenta":	"785623",
                                        "Saldo":	21000000
                                    }, 
                                    {
                                        "Id":	"131321",
                                        "Nombre":	"Adela Dominguez",
                                        "NumCuenta":	"9638528",
                                        "Saldo":	17000000
                                    },                           
                                    {
                                        "Id":	"131741",
                                        "Nombre":	"Hernan Fontalvo",
                                        "NumCuenta":	"789456",
                                        "Saldo":	45000000
                                    }
                        ]
                    })

with open('ahorradores.json','w') as file:
    json.dump(data, file, indent = 4)

print(data) 