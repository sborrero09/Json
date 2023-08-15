import json
with open('servicios.json') as misEmpleados:
    data = json.load(misEmpleados)

    for usuario in data['usuarios']:
        print('full name', usuario{'full_name'})
        print('email', usuario{'email'})
        print('Total packages per user', usuario{'total_packages'})
        print('Total price:', usuario{'total_price'})
        print("")
        print()