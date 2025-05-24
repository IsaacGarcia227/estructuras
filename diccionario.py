
class MiDiccionario:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def hash(self, clave):
        return hash(clave) % self.size
    
    def agregar(self, clave, valor):
        indice = self.hash(clave)
        self.table[indice] = valor
    
    def obtener(self, clave):
        indice = self.hash(clave)
        return self.table[indice]
