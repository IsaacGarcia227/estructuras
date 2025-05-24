from pila import Pila
from cola import Cola
from arbol import Nodo
from arbol import ArbolBinario
from diccionario import MiDiccionario


print("Inserción en listas")

primitiva = [1, 2, 3, 4]
primitiva.append(5)
primitiva.append(5)
primitiva.remove(5)
print(primitiva)
primitiva.pop(1)
print(primitiva)



#Pilas, pilas

print("Inserción en pilas")
tinaco = Pila()
tinaco.apilar(5)
tinaco.apilar(6)
tinaco.apilar(8)

tinaco.imprime_valores()
tinaco.desapilar()
tinaco.imprime_valores()
tinaco.desapilar()
tinaco.imprime_valores()
tinaco.desapilar()
tinaco.imprime_valores()
tinaco.desapilar()
tinaco.imprime_valores()


#colas #colas #colas #colas #colas #colas

print("colas")

tortillas = Cola()
tortillas.encolar("Doña Petra")
tortillas.encolar("Carlitos")
tortillas.encolar("piterman")
tortillas.imprime_cont()

tortillas.desencolar()
tortillas.imprime_cont()
tortillas.desencolar()
tortillas.imprime_cont()
tortillas.desencolar()
tortillas.imprime_cont()
tortillas.desencolar()

#arboles #arboles #arboles #arboles #arboles
print("arboles")
numeros = ArbolBinario()
numeros.insertar(2)
numeros.insertar(3)
numeros.insertar(1)
numeros.insertar(0)
numeros.insertar(7)
print(numeros)

# Diccionarios # Diccionarios # Diccionarios
print("Diccionarios")

ferreteria = MiDiccionario()
ferreteria.agregar("bafer", 4)
ferreteria.agregar("talabro", 6)
ferreteria.agregar("cerrucho", 2)
ferreteria.agregar("brocas", 20)
ferreteria.agregar("mesas", 2)

cantidadBrocas = ferreteria.obtener("brocas")
cMesas = ferreteria.obtener("mesas")
print(cantidadBrocas)
print(cMesas)
#ferreteria.hash(4)



