class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
    
    def __str__(self):
        print(f"La marca es: {self.marca}\nEl modelo es: {self.modelo}\nEn marcha: {self.enmarcha}")

miCarro1=Vehiculos("Toyota", "Canry")

print(miCarro1)