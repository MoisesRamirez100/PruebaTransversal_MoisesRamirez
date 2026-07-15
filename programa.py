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

#Programa principal
def main():
    while True:
        menu()
        opc=leer_opc()

        if opc==1:
            categoria=input("Que categoria desea buscar: ").lower().strip()
            unidades_cat(categoria, prendas, bodega)

main()