class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
    def presentarse(self):
        print(f" ¡Hola! Soy {self.nombre}, artista de {self.genero}")
    def actuar(self):
        print(" El artista está actuando...")
    def despedirse(self):
        print(f" ¡Gracias por su apoyo! ¡Hasta pronto!")
class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular
    def actuar(self):
        print(f" {self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")
class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo
    def actuar(self):
        print(f" El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")
class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes
    def actuar(self):
        print(f" La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")
def iniciar_festival(lista_artistas):
    print("\n" + "="*50)
    print("¡COMIENZA EL FESTIVAL MUSICAL! ")
    print("="*50)
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("\n Fin de la actuación \n")
def main():
    artistas = []
    
    print("FESTIVAL MUSICAL")
    print("-" * 25)
    try:
        cantidad = int(input("¿Cuántos artistas se presentarán? "))
    except:
        print("Número inválido. Usando 1 artista por defecto.")
        cantidad = 1
    for i in range(cantidad):
        print(f"\n Artista {i+1}:")
        tipo = input("Tipo (Cantante/DJ/Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        try:
            popularidad = int(input("Popularidad (1-100): "))
        except:
            print("Popularidad inválida. Usando 50 por defecto.")
            popularidad = 50
        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo de mezcla: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "banda":
            try:
                integrantes = int(input("Número de integrantes: "))
            except:
                print("Número inválido. Usando 4 por defecto.")
                integrantes = 4
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print("Tipo desconocido. Creando artista genérico.")
            artista = Artista(nombre, genero, popularidad)
        artistas.append(artista)
    iniciar_festival(artistas)
if __name__ == "__main__":
    main()