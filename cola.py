
class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, item):
        self.cola.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            print("La cola está vacía.")
    
    def esta_vacia(self):
        return len(self.cola) == 0

    def imprime_cont(self):
        print(self.cola)