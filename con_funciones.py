print("------------------------------")
print("-BUSCAR UN NUMERO EN CONJUNTO-")
print("------------------------------")

#definicion de la funcion
def buscardatoenlista(datoabuscar,lista):
    r = False
    for i in lista:
        if i == datoabuscar:
            r =True
    return r

#entrada
dato = int (input("numero a buscar: ")) #se recibe el dato del usuario

#procesamiento
lista = [1,2,3,4,5] #se almacena una lista de datos
if buscardatoenlista(dato,lista):
    print(" lo encontre")
else:
    print("no lo  encontre")

#salida
print("\nEso era...")
