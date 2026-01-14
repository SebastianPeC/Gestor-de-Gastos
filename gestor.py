import csv
def agregar_gasto():
    #pido los datos del gasto a agregar y los almaceno en una lista
    descripcion = input('ingresa descripcion: ')
    categoria = input('ingresa categoria: ')
    monto = input('ingresa monto sin puntos: ')
    fecha = input('ingresa fecha (dd/mm/aa):')
    gasto = [descripcion,categoria,monto,fecha]

    #abro el archivo para trabajar con sus datos
    with open('datos\\gastos.csv',newline='',encoding='utf-8') as f:
        lista = list(csv.reader(f, delimiter=','))
        #verifico cual es el ultimo id y lo almaceno en una variable
        ultimo_id = int(lista[-1][0])
    
    #agrego el id a la lista con los nuevos datos
    gasto.insert(0,ultimo_id+1)
    
    #abro el archivo para agregarle el nuevo gasto
    with open('datos\\gastos.csv','a',newline='',encoding='utf-8') as f:
        escribir = csv.writer(f, delimiter= ',')
        escribir.writerow(gasto)

def leer_gastos():
    with open('datos\\gastos.csv',newline='',encoding='utf-8') as f:
        lista = list(csv.reader(f, delimiter=','))
    
    for i in range(1, len(lista)):
        print(f'para el gasto {lista[i][0]}')
        for j in range(len(lista[i])):
            print(f'{lista[0][j]}: {lista[i][j]}')
        print('\n')

def buscar_gasto():
    while True:
        try:
            with open('datos\\gastos.csv',newline='',encoding='utf-8') as f:
                lista = list(csv.reader(f, delimiter=','))

            ingreso = int(input('si quiere buscar por id ingrese 1\nsi quiere buscar por categoria ingrese 2\ningrese aqui:'))
            if ingreso == 1:
                id = input('ingresa id: ')
                for i in range(1, len(lista)):
                    if id == lista[i][0]:
                        print(f'\ninformacion del gasto {i}:')
                        for j in range(len(lista[i])):
                            print(f'{lista[0][j]}: {lista[i][j]}')
                        estado = True
                        break
                    else:
                        estado = False
                if estado == True:
                    print('el gasto se ha hallado con exito\n')
                else:
                    print(f'el gasto con el id {i} no existe\n')

            elif ingreso == 2:
                categoria = input('ingresa la categoria: ')
                for i in range(1, len(lista)):
                    if categoria == lista[i][2]:
                        print(f'\ninformacion del gasto {i}:')
                        for j in range(len(lista[i])):
                            print(f'{lista[0][j]}: {lista[i][j]}')
                        estado = True
                    else:
                        estado = False
                if estado == True:
                    print('el gasto se ha hallado con exito\n')
                else:
                    print(f'el gasto con la categoria {i} no existe\n')

            else:
                raise ValueError
        except ValueError:
            print('intenta con un numero valido')

def modificar_gasto():
    #abro el archivo para trabajar sus datos
    with open('datos\\gastos.csv',newline='',encoding='utf-8') as f:
        lista = list(csv.reader(f, delimiter=','))

    #pido el id del gasto a modificar
    gasto_a_modificar = int(input('ingrese el id del gasto a modificar: '))

    #verifico que el gasto a modificar exista
    if gasto_a_modificar > len(lista) or gasto_a_modificar < 1:
        print("el gasto a modificar no existe")
    
    else:
        #hago un ciclo para recorrer gastos.csv (excluyendo los nombres de las columnas)
        for i in range(1, len(lista)):

            #verifico si el id ingresado es igual a i en este ciclo
            if int(lista[i][0]) != gasto_a_modificar:
                continue
            
            #si es igual hago lo siguiente:
            else:

                print('el gasto que va a modificar tiene los siguientes datos:')
                #ciclo que imprime los nombres de las columnas seguidas de los datos del gasto a modificar
                for j in range(len(lista[0])):
                    print(f'{lista[0][j]}: {lista[i][j]}')

                #pido los nuevos datos y los almaceno en una lista
                nueva_descripcion = input('ingresa nueva descripcion: ')
                nueva_categoria = input('ingresa nueva categoria: ')
                nuevo_monto = input('ingresa nuevo monto sin puntos ni comas: ')
                nueva_fecha = input('ingresa nueva fecha(dd/mm/aa): ')
                gasto = [gasto_a_modificar,nueva_descripcion,nueva_categoria,nueva_fecha,nuevo_monto]

                #elimino el gasto anterior
                lista.pop(gasto_a_modificar)
                #agrego el gasto con los nuevos datos en el lugar del gasto borrado
                lista.insert(gasto_a_modificar,gasto)

                #abro el archivo para cambiar su contenido por la lista de gastos modificada
                with open('datos\\gastos.csv','w',newline='',encoding='utf-8') as f:
                    nuevo = csv.writer(f, delimiter=',')
                    nuevo.writerows(lista)
                print(f'el gasto {gasto_a_modificar} ha sido modificado exitosamente')
                break