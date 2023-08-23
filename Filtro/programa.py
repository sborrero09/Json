import json
import os

data = []

def openFile():
    with open("./Filtro/manuales.json","r") as file:
        data = json.load(file)
    return data
listado = openFile
def saveFile(data):
    with open("./Filtro/manuales.json", "w", encoding="utf-8") as file:
        json.dump(data,file, indent=4,)
    
def validarMenu(msj):
    while True:
        try:
            op=int(input(msj))
            if op=='': 
                print('Ingrese alguna opcion')
                input('enter...\n')
                continue
            return op
        except Exception:
            print('solo se aceptan datos numericos')

def menu():
    nexx=True
    conf=True
    while nexx:
        os.system('clear')
        print(' '*16,"***MENÚ***\n")
        print("\t1.Crear\n\
        2.Modificar\n\
        3.Eliminar\n\
        4.Listar\n\
        5.Generar informe de datos.txt\n\
        6.Salir\n")

        op = validarMenu('Ingrese una opción del menu anterior: ')
        if op == 6:
            nexx = False
            return print('Ha salido exitosamente del programa.')
        elif op < 1 or op > 6:
            print('Opcion inválida escoja un nùmero entre el 1 y el 6')
            input('Presione cualquier tecla para continuar...')
            conf = False
        if conf == True:
          switch = {1:Crear,2:Modificar,3:Eliminar,4:Listar,5:GenerarTxt}
          switch[op]()
          menu()

    
def Crear():
    os.system('clear')
    print("""
        1.Manuales
        2.Temas
             """)
    op = validarMenu('Ingrese una opción del menu inmediato: ')
    if op < 1 or op > 2:
            print('Número inválido')
            input('Presione cualquier tecla para continuar...')
    if op == 1:
        print("A continuación creará un manual")
        manual = input('Ingrese el nombre del manual: ')
        author = input('Ingrese el author: ')
        pags = input('Ingrese la cantiudad de paginas: ')

        data["manuales"][{
        "":manual,
        "author":author,
        "paginas":pags,
    }]
    
    elif op == 2:
        print("A continuación creará unos temas")
    nomtem = input("Ingrese el nombre del manual al cual desea agregar sus temas")
    titulo1 = input('Ingrese el titulo del primer tema: ')
    clasif1 = input('Ingrese la clasficación del primer tema: ')
    titulo2 = input('Ingrese el titulo del segundo tema: ')
    clasif2 = input('Ingrese la clasficación del segundo tema: ')
    titulo3 = input('Ingrese el titulo del tercer tema: ')
    clasif3 = input('Ingrese la clasficación del tercer tema: ')


    data["temas"]({
        "temas":[{titulo1,clasif1},{titulo2,clasif2},{titulo3,clasif3}]
    })
    saveFile()
    

def Modificar():
    openFile()
    print("""
        1.Manuales
        2.Temas
             """)
    op = validarMenu('Ingrese una opción del menu inmediato: ')
    if op < 1 or op > 2:
            print('Número inválido')
            input('Presione cualquier tecla para continuar...')
    if op == 1:
            print("A continuación modificarà el manual que desee")
            nom = input("Ingrese el nombre del manual que desea modificar: ")
            manual_eliminado = listado['manuales'].pop(nom)
            print(f"El manual '{manual_eliminado['manuales']}' ha sido eliminado."); saveFile(listado)

    if op == 2:
        print("A continuación mofificarà los temas que desee")
        nom = input("Ingrese el nombre del manual al cual desea modificar sus temas: ")
    tema_eliminado = listado['manuales'].pop(nom)
    print(f"Los temas '{tema_eliminado['manuales']}' has sido eliminados."); saveFile(listado)

def Listar():
    
    openFile()
    print("""
        1.Manuales
        2.Temas
             """)
    op = validarMenu('Ingrese una opción del menu inmediato: ')

    if op < 1 or op > 2:
            print('Número inválido')
            input('Presione cualquier tecla para continuar...')
    if op == 1:
        print("|Manual      |Author           |Paginas      |")
    for index,abc in enumerate(['manuales'],start=1):
            temas = ', '.join(abc["temas"])
            print()
            print[index, abc["manuales"],'|',abc["author"],'|',abc["paginas"],'|']
            input('\nPresione cualquier tecla para volver al menu...\n')

    if op == 2:
        print("{:^9} {:^10} {:^10} {:^9} {:^9}".format('Temas |'))
        for index,abc in enumerate(['manuales'],start=1):
                temas = ', '.join(abc["temas"])
                print()
                print("{:1} {:<9} {:<1} {:<14} {:<1} {:<10} {:<1} {:<6} {:<1} {:<12}".format(temas))
                input('\nPresione cualquier tecla para volver al menu...\n')



def Eliminar():
    openFile()
    print("""
        1.Manuales
        2.Temas
             """)
    op = validarMenu('Ingrese una opción del menu inmediato: ')
    if op < 1 or op > 2:
            print('Número inválido')
            input('Presione cualquier tecla para continuar...')
    if op == 1:
        print("A continuación eliminará el manual que desee")
        nom = input("Ingrese el nombre del manual que desea eliminar: ")
        manual_eliminado = listado['manuales'].pop(nom)
        print(f"El manual '{manual_eliminado['manuales']}' ha sido eliminado."); saveFile(listado)

    if op == 2:
        print("A continuación eliminará los temas que desee")
        nom = input("Ingrese el nombre del manual al cual desea eliminar sus temas: ")
        tema_eliminado = listado['manuales'].pop(nom)
        print(f"Los temas '{tema_eliminado['manuales']}' has sido eliminados."); saveFile(listado)



def GenerarTxt():
    pass

menu()