
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía.")
    
    def esta_vacia(self):
        return len(self.items) == 0

    def imprime_valores(self):
        print(self.items)