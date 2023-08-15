import json
def validarNom(msj):     
    data = input(msj)     
    while(data.strip() == ''):        
         print("\nIngrese algún dato\n")        
         data = input(msj)     
    return data 
    
def validarInt(msj):     
    while True:       
        try:            
            id=int(input(msj))        
            if id=='':                
                print('intentelo de nuevo\n')                       
                continue         
            return id     
        except Exception:           
            print('ingrese un dato correcto correcta')

data = {}
data['jugadores'] = []

a = True

while a:
    data['jugadores'].append({
        'nom' : input("Nombre: "),
        'edad' : (input("Edad: ")),
        'peso' : (input("Peso en kg: "))
        })
    op = int(input("Ingrese 1 para continuar; 0 para salir: "))
    if op == 1:
        continue
    if op == 0:
        print("Fin de programa")
        a = False

with open('jugadores.json','w') as file:
    json.dump(data, file, indent = 4)

print(data) 