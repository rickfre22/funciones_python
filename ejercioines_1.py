# construir una fucion que reciba su nombre com parametro y que muestre 5 veces en pantalla

def  repetirnombre(nombre):
    for i in range(1,6):
        print(f"{i} . {nombre}")

#entrada

nombre = input("digite su nombre:")

repetirnombre(nombre)

print("\nEso era...")
    
