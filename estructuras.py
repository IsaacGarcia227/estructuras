
class MiLista:
    def __init__(self):
        self.lista = []
    
    def agregar(self, elemento):
        self.lista.append(elemento)
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print(f"{elemento} no encontrado en la lista.")
    
    def mostrar(self):
        print(self.lista)
