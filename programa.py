import time

#diccionarios
prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}


#Funciones del menu
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoria")
    print("2. Busqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")

def leer_opc():
    while True:
        try:
            opc=int(input("- "))
            if opc>=1 and opc<=6:
                return opc
            else:
                print("Ingrese una opción valida")
        except ValueError:
            print("Debe ingresar un número entero")

#Opcion 1
def unidades_cat(categoria, prendas, bodega):
    #se inicia la lista
    unidades=0
    #bucle for para encontrar claves con esa categoria
    for clave, valor in prendas.items():
        if valor[1]==categoria:
            unidades+=bodega[clave][1]
    
    print(f"Hay {unidades} unidades de la categoria {categoria}")

#Opcion 2
def busqueda_precio(p_min, p_max, prendas, bodega):
    lista=[]
    for clave, valor in bodega.items():
        #Si el valor esta dentro del rango de precios, y tiene unidades añadir a la lista
        if valor[0]>=p_min and valor[0]<= p_max and valor[1]!=0:
            lista.append(f"{clave}--{prendas[clave][0]}")
    #Detectar si la lista esta vacia
    if len(lista)==0:
        print("No hay prendas en ese rango de precios")
    #Ordenar y mostrar si tiene contenido
    else:
        lista.sort()
        print(lista)

#Programa principal
def main():
    while True:
        menu()
        opc=leer_opc()

        if opc==1:
            categoria=input("Que categoria desea buscar: ").lower().strip()
            unidades_cat(categoria, prendas, bodega)

        elif opc==2:
            while True:
                try:
                    p_min=int(input("Ingrese el precio minimo: "))
                    if not p_min>=0:    
                        print("Debe ser mayor o igual a cero")
                        continue 
                    p_max=int(input("Ingrese el precio maximo: "))
                    if not p_max>p_min:
                        print("Debe ser mayor al precio minimo")
                        continue
                    busqueda_precio(p_min, p_max, prendas, bodega)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")


main()