# CODIGO ERP 
import csv
import pandas as pd
import seaborn
import matplotlib.pyplot as plt

def menu():
    print("***ACCIONES DE ERP DISPONIBLES**")
    print("1. VER HISTÓRICO DE DATOS ----------- 2. AÑADIR UNA NUEVA UNIDAD")
    print("3. MODIFICAR REGISTRO ----------- 4. ELIMINAR CODIGO O ARTICULO")
    print("5. LOCALIZAR ARTICULO POR CODIGO ----------- 6. LOCALIZAR ARTICULO POR NOMBRE")
    print("7. REALIZAR UN REPORTE ----------- 8. RELLENAR ESPACIOS VACÍOS")
    print("9. SALIR")
    option = input("Introduzca el número de la opción deseada: ")
    return option

def LeerCodigo(codigo):
    with open('ERP_BDD.csv', 'r') as openfile:
        reader = csv.reader(openfile)
        for row in reader:
            if codigo == row[0]:
                return row
        return "NO EXISTE"

def VerHistorico():
    with open('ERP_BDD.csv', 'r') as openfile:
        reader = csv.reader(openfile)
        for row in reader:
            print(row)

def AñadirUnidadNueva():
    codigo = input('Ingrese código de nueva unidad: ')
    if LeerCodigo(codigo) == "NO EXISTE":
        codigo = input('Ingrese codigo: ')
        familia = input('Ingrese familia: ')
        subfamilia = input('Ingrese subfamilia: ')
        categoria = input('Ingrese categoria: ')
        subcategoria = input('Ingrese subcategoria: ')
        descripcion = input('Ingrese descripcion: ')
        coste = input('Ingrese coste: ')
        venta = input('Ingrese venta: ')
        with open('ERP_BDD.csv', 'a') as openfile:
            writer = csv.writer('\n' '+codigo+', '+familia+', '+subfamilia+', '+categoria+', '+subcategoria+', '+descripcion+', '+coste+', '+venta')
    else:
        print('ERROR: PRODUCTO EXISTENTE EN LA BASE DE DATOS')

def ModificarProducto():
    codigo = input('Ingrese el codigo a modificar: ')
    if LeerCodigo(codigo)=="NO EXISTE":
        print('ERROR: EL CODIGO QUE INTENTA MODIFICAR NO EXISTE')
    else:
        familia = input('Ingrese familia: ')
        subfamilia = input('Ingrese subfamilia: ')
        categoria = input('Ingrese categoria: ')
        subcategoria = input('Ingrese subcategoria: ')
        descripcion = input('Ingrese descripcion: ')
        coste = input('Ingrese coste: ')
        venta = input('Ingrese venta: ')
        modificarBD(codigo, familia, subfamilia, categoria, subcategoria, descripcion, coste, venta)

def modificarBD(codigo, familia, subfamilia, categoria, subcategoria, descripcion, coste, venta):
    result = []
    with open('Almacen_clasificado_definitivo.csv', 'r') as openfile:
        reader = csv.reader(openfile)
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['familia']=familia
                row['subfamilia']=subfamilia
                row['categoria']=categoria
                row['subcategoria']=subcategoria
                row['descripcion']=descripcion
                row['coste']=coste
                row['venta']=venta
            result.append(row)
    with open('ERP_BDD.csv', 'a') as openfile:
        fieldnames = ['codigo', 'familia', 'subfamilia', 'categoria', 'subcategoria', 'descripcion', 'coste', 'venta']
        writer = csv.writer(openfile, fieldnames=fieldnames, extrasaction='ignore')

def EliminarProducto():
    codigo = input('Ingrese codigo a eliminar: ')
    if LeerCodigo(codigo)=="NO EXISTE":
        print('ERROR: EL CODIGO QUE DESEA ELIMINAR NO FIGURA EN LA BASE DE DATOS')
    else:
        eleccion = input('Si está seguro SI=S NO=N')
        if eleccion=='S':
            eliminar_articulo_BD(codigo)
        else:
            return menu()

def eliminar_articulo_BD(codigo):
    result = []
    password = str(input('Ingrese la contraseña para eliminar artículo: '))
    if password == "1234":
        with open('ERP_BDD.csv') as openfile:
            reader = csv.reader(openfile)
        with open('ERP_BDD.csv', 'a') as openfile:
            writer = csv.writer(openfile)
            for row in reader:
                if row[0] == codigo:
                    result['codigo'] = row[0]
                    result['familia'] = row[1]
                    result['subfamilia'] = row[2]
                    result['categoria'] = row[3]
                    result['subcategoria'] = row[4]
                    result['descripcion'] = row[5]
                    result['coste'] = row[6]
                    result['venta'] = row[7]
    return result

def BuscarProducto():
    codigo = input('Ingrese el código de producto que desea buscar: ')
    if LeerCodigo(codigo)=="NO EXISTE":
        print('El código de producto que desea buscar no existe en la base de datos')
    else:
        BuscarBD(codigo)

def BuscarBD(codigo):
    result = []
    with open('ERP_BDD.csv', 'r') as openfile:
        reader = csv.reader(openfile)
        for row in reader:
            if row['codigo']==codigo:
                print('' + str(row['codigo']) + '/t' + str(row['familia']) + '/t' + str(row['subfamilia'])
                + '/t'+ str(row['categoria']) + '/t' + str(row['subcategoria']) + '/t' + str(row['descripcion']) + '/t'
                + str(row['coste']) + '/t' + str(row['venta']))
        else: print("NO EXISTE")

def BuscarPorNombre():
    df = pd.read_csv('ERP_BDD.csv')
    palabra = str(input('Ingrese el nombre a filtrar: '))
    print(df[df['descripcion'].str.contains(palabra)])

def ReporteCodigoPrecio():
    df = pd.read_csv('ERP_BDD.csv')
    ord = df.sort_values(by=['codigo'])[['codigo', 'coste', 'venta']]
    print(ord)

def RellenarEspacios():
    codigo=input('Ingrese codigo de producto a rellenar: ')
    if LeerCodigo(codigo)=="NO EXISTE":
        print('Error: El código que desea eliminar no existe')
    else:
        RellenarBD(codigo)

def RellenarBD(codigo):
    result=[]
    with open('ERP_BDD.csv', 'r') as openfile:
        reader = csv.reader(openfile)
        codigo = 'codigo'
        categoria = 'categoria'
        subcategoria = 'subcategoria'
        familia = 'familia'
        subfamilia = 'subfamilia'
        descripcion = 'descripcion'
        coste = 'coste'
        venta = 'venta'
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=codigo
                if row['familia']=="":
                    row['familia']=familia
                else:
                    row['familia']=row['familia']
                if row['subfamilia']=="":
                    row['subfamilia']=subfamilia
                else:
                    row['subfamilia']=row['subfamilia']
                if row['categoria']=="":
                    row['categoria']=categoria
                else:
                    row['categoria']=row['categoria']
                if row['subcategoria']=="":
                        row['subcategoria']=subcategoria
                else:
                    row['subcategoria']=row['subcategoria']
                if row['descripcion']=="":
                    row['descripcion']=descripcion
                else:
                    row['descripcion']=row['descripcion']
                if row['coste']=="":
                    row['coste']=coste
                else:
                    row['coste']=row['coste']
                if row['venta']=="":
                    row['venta']=venta
                else:
                    row['venta']=row['venta']
            result.append(row)
    with open('ERP_BDD.csv','w') as File:
        fieldnames=['codigo', 'familia', 'subfamilia', 'categoria', 'subcategoria', 'descripcion', 'coste', 'venta']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

def articulo_eliminado_BD(codigo, familia, subfamilia, subcategoria, descripcion, coste, venta):
    result=[]
    password=str(input('Ingrese la contraseña para eliminar artículo: '))
    if password=="1234":
        with open('ERP_BDD.csv') as openfile:
            reader = csv.reader(openfile)
        with open('ERP_BDD.csv', 'a') as openfile:
            writer= csv.writer(openfile)
            eleccion='S'
            for row in reader:
               if row['codigo']==codigo:
                row['codigo']=codigo
                row['familia']=familia
                row['subfamilia']=subfamilia
                row['subcategoria']=subcategoria
                row['descripcion']=descripcion
                row['coste']=coste
                row['venta']=venta
            result.append(row)

def main():
    while True:
        option = menu()
        if option == '1':
            VerHistorico()
        elif option =='2':
            AñadirUnidadNueva()
        elif option =='3':
            ModificarProducto()
        elif option == '4':
            EliminarProducto()
        elif option == '5':
            BuscarProducto()
        elif option == '6':
            BuscarPorNombre()
        elif option == '7':
            ReporteCodigoPrecio()
        elif option == '8':
            RellenarEspacios()
        elif option == '9':
            break
    return

main()