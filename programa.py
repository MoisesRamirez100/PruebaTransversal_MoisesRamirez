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
    print("=====================================")

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
        if valor[1].lower().strip()==categoria.lower().strip():
            unidades+=bodega[clave][1]
    
    print(f"El total de unidades disponibles es: {unidades}")

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
        print(f"Las prendas encontradas son: {lista}")

#Opcion 3
def buscar_cod(codigo, bodega):
    if codigo in bodega:
        return True
    return False

def actualizar_precio(codigo, p_nuevo, bodega):
    if buscar_cod(codigo, bodega):
        bodega[codigo][0]=p_nuevo
        return True
    return False

#Opcion 4

#Validaciones
def validar_texto(texto):
    if texto.strip()=="":
        return False
    return True

def validar_unisex(es_unisex):
    if not es_unisex in("s", "n"):
        return False
    return True

def validar_precio(precio):
    if precio>0:
        return True
    return False

def validar_unidades(unidades):
    if unidades>=0:
        return True
    return False

#Agregar la prenda
def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
    #Primero verificar que el codigo no este registrado
    if codigo in prendas:
        return False
    else:
        #Pasar el es_unisex a booleano
        if es_unisex=="s":
            es_unisex=True
        elif es_unisex=="n":
            es_unisex=False

        #Asignar los valores para cada diccionario
        valor_prendas=[nombre, categoria, talla, color, material, es_unisex]
        valor_bodega=[precio, unidades]

        #Agregar prenda a los diccionarios

        prendas[codigo]=valor_prendas
        bodega[codigo]=valor_bodega
        return True

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

        elif opc==3:
            while True:
                codigo=input("Ingrese el codigo de la prenda a actualizar: ").upper().strip()
                try:
                    p_nuevo=int(input("Ingrese el nuevo precio: "))
                    if p_nuevo<=0:
                        print("El precio nuevo debe ser un valor entero positivo")
                        continue
                except ValueError:
                    print("El precio nuevo debe ser un valor entero positivo")

                if actualizar_precio(codigo, p_nuevo, bodega):
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
                
                opc=input("¿Desea actualizar otro precio (s/n)?: ").lower().strip()
                if opc=="s":
                    continue
                else:
                    break    
        elif opc==4:
            while True:
                #Solicitud y validacion de variables de texto basicas
                codigo=input("Ingrese el codigo: ").upper()
                if not validar_texto(codigo):
                    print("El codigo no deber ser vacio ni solo espacios en blanco")
                    break
                nombre=input("Ingrese el nombre: ").capitalize()
                if not validar_texto(nombre):
                    print("El nombre no debe ser vacio ni solo espacios en blanco")
                    break
                categoria=input("Ingrese la categoria: ").lower()
                if not validar_texto(categoria):
                    print("La categoria no debe ser vacia ni solo espacios en blanco")
                    break
                talla=input("Ingrese la talla: ").upper()
                if not validar_texto(talla):
                    print("La talla no debe ser sre vacia ni solo espacios en blanco")
                    break
                color=input("Ingrese el color: ").lower()
                if not validar_texto(color):
                    print("El color no debe ser vacio ni solo espacios en blanco")
                    break
                material=input("Ingrese el material: ").lower()
                if not validar_texto(material):
                    print("El material no debe ser vacio ni solo espacios en blanco")
                    break
                #Validacion de unisex
                es_unisex=input("Ingrese si es unisex (s/n): ").lower()
                if not validar_unisex(es_unisex):
                    print("Debe ingresar s/n")
                    break
                #Validacion de numeros
                try:
                    precio=int(input("Ingrese el precio: "))
                    if not validar_precio(precio):
                        print("El precio debe ser un numero entero mayor a cero")
                        break
                    unidades=int(input("Ingrese las unidades: "))
                    if not validar_unidades(unidades):
                        print("Las unidades deben ser un entero mayor o igual a cero")
                        break
                except ValueError:
                    print("Se debe ingresar un numero entero")
                    break
                
                #Si todo ha sido validado agregar la prenda
                if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, prendas, bodega):
                    print("Prenda agregada")
                else:
                    print("El codigo ya existe")
                break


        elif opc==5:
            print("nada")

        elif opc==6:
            print("Programa finalizado.")
            time.sleep(3)
            break
main()