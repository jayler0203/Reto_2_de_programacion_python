import random
class Personaje:

    def __init__(self, nombre, fuerza, defensa , vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = vida

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def esta_vivo(self):
        return self.vida > 0    

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
    def cambiar_estadistica(self, estadistica, nuevo_valor):
        if estadistica == 'fuerza':
            self.fuerza = nuevo_valor
        elif estadistica == 'defensa':
            self.defensa = nuevo_valor
        elif estadistica == 'vida':
            self.vida = nuevo_valor
        else:
            print("Estadística no válida")
class Protagonista(Personaje):


    def __init__(self, nombre, fuerza, defensa, vida):
        super().__init__(nombre, fuerza, defensa, vida)

    def usar_objeto(self, objeto):
        # Logic to use an object and potentially modify attributes
        print(self.nombre, "ha usado el objeto:", objeto)
class Enemigo(Personaje):
    def __init__(self, nombre, fuerza, defensa, vida, objeto_recompensa):
        super().__init__(nombre, fuerza, defensa, vida)
        self.objeto_recompensa = objeto_recompensa

    def obtener_objeto_recompensa(self):
        return self.objeto_recompensa
class objeto:
    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    def efecto(self):
        print("")     
class Pocion(objeto):
    def __init__(self, nombre, descripcion):
        super().__init__(nombre, descripcion)

    def efecto(self, protagonista):
        if random.random() < 0.5:
            protagonista.vida = 0
            print("Has sido envenenado.")
            protagonista.morir()
        else:
            protagonista.vida = 100
            print("La poción te ha curado por completo. ¡Estás lleno de energía!") 
def combate(personaje_1, personaje_2):
    turno = 0
    while personaje_1.esta_vivo() and personaje_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", personaje_1.nombre,":")
        personaje_1.atacar(personaje_2)
        print(">>> Acción de ", personaje_2.nombre,":")
        personaje_2.atacar(personaje_1)
        turno = turno + 1
    if personaje_1.esta_vivo():
        print("\nHa ganado", personaje_1.nombre)
    else:
        print("\nHa ganado", personaje_2.nombre)
class JuegoAventura:
    def comenzar(self):
        aventura=True
        print("¡Bienvenido a la Isla del Tesoro!")
        nombre_jugador = input("Por favor, introduce el nombre de tu jugador: ")
        protagonista = Protagonista(nombre_jugador, 30, 15, 100)

        print("Hola, " + protagonista.nombre + ". Comencemos la aventura.")
        print("Te encuentras en la playa de la isla.")
        print("Desde aquí, tienes tres opciones:")

        while True:
            print("1. Explorar el pantano")
            print("2. Adentrarse en la selva")
            decision = input("Elige una opción: ")

            if decision == '1':
                self.explorar_pantano(protagonista)
                break
            elif decision == '2':
                self.adentrarse_selva( protagonista)
                break

                
            else:
                print("Opción no válida. Por favor, elige nuevamente.")
            
    def final_juego(self, protagonista , tesoro_encontrado=False ):
        if protagonista.esta_vivo():
            if tesoro_encontrado:
                print("¡Has encontrado el tesoro y has ganado!")
                
            else:
                print("No has encontrado el tesoro. Mejor suerte la próxima vez.")
        else:
            print("Has muerto. El juego ha terminado.")

        print("¡Has alcanzado el final del juego! Gracias por jugar.\n\n\n")

    def explorar_pantano(self, protagonista):

        print("Decides explorar el pantano.")
        print("Encuentras un pequeño slime que se abalanza sobre ti. Debes enfrentarlo.")

        enemigo_debil = Enemigo("Criatura", 15, 5, 15, "Garra afilada")
        combate(protagonista, enemigo_debil)

        if not protagonista.esta_vivo():
            self.final_juego(protagonista)
            return

        print("La criatura en el pantano ha dejado una poción desconocida como recompensa.")

        print("¿Quieres beber la poción desconocida?")
        print("1. Sí")
        print("2. No")

        decision = input("Elige una opción: ")

        if decision == '1':
            poción = Pocion("Poción misteriosa", "Una poción con efectos desconocidos")
            poción.efecto(self)
        elif decision == '2':
            print("Decides no beber la poción y sigues explorando el pantano.")

        if not protagonista.esta_vivo():
            self.final_juego(protagonista)
            return

        print("Continúas explorando el pantano y encuentras un monstruo gigante.")

        print("¿Qué decides hacer?")
        print("1. Enfrentar al monstruo gigante")
        print("2. Intentar escapar de la isla sin el tesoro")

        decision = input("Elige una opción: ")

        if decision == '1':
            print("Decides enfrentar al monstruo gigante.")
            monstruo_gigante = Enemigo("Monstruo Gigante", 40, 20, 50, "Garra devastadora")
            combate(protagonista, monstruo_gigante)

            if not protagonista.esta_vivo():
                self.final_juego(protagonista)
                return
            else:
                print("Has vencido al monstruo gigante.")
        elif decision == '2':
            print("Intentas escapar de la isla")
            self.final_juego(protagonista)

        print("Continúas explorando pero no encuentras nada más interesante.")
        self.final_juego(protagonista)
    def adentrarse_selva(self,protagonista):
        print("Decides adentrarte en la selva.")
        print("Encuentras un río con un puente colgante. ¿Qué decides hacer?")
        print("1. Cruzar el puente")
        print("2. Seguir explorando la selva")

        decision = input("Elige una opción: ")

        if decision == '1':
            print("Cruzas el puente pero sigues perdido.")
            print("Encuentras un esqueleto. Debes enfrentarlo.")

            esqueleto = Enemigo("Esqueleto", 20, 10, 25, "Espada oxidada")
            combate(protagonista, esqueleto)

            if not protagonista.esta_vivo():
                self.final_juego(protagonista)
                return

            print("El esqueleto ha dejado una espada maldita como recompensa.")

            print("¿Quieres equipar la espada maldita?")
            print("1. Sí")
            print("2. No")

            decision = input("Elige una opción: ")

            if decision == '1':
                print("Decides equipar la espada.")
                print("Te has convertido en un esqueleto.")
                self.final_juego(protagonista)
                return
            elif decision == '2':
                print("Decides no equipar la espada maldita y sigues explorando la selva.")

        if not protagonista.esta_vivo():
            print("Has sido derrotado.")
            self.final_juego(protagonista)
            return

        print("Continúas explorando la selva y ves un esqueleto pasando un esqueleto.")
        print("El esqueleto ha dejado una poción misteriosa como recompensa.")

        print("¿Quieres beber la poción misteriosa?")
        print("1. Sí")
        print("2. No")

        decision = input("Elige una opción: ")

        if decision == '1':
            poción = Pocion("Poción misteriosa", "Una poción con efectos desconocidos")
            poción.efecto(protagonista)
            if not protagonista.esta_vivo():
                self.final_juego(protagonista)
                return
        elif decision == '2':
            print("Decides no beber la poción y sigues explorando la selva.")

        print("Continúas explorando la selva y encuentras al capitán de los esqueletos.")

        print("¿Qué decides hacer?")
        print("1. Enfrentar al capitán de los esqueletos")
        print("2. Intentar escapar de la isla sin el tesoro")

        decision = input("Elige una opción: ")

        if decision == '1':
            print("Decides enfrentar al capitán de los esqueletos.")
            capitán_esqueletos = Enemigo("Capitán Esqueletos", 40, 20, 30, "llave")
            combate(protagonista, capitán_esqueletos)

            if not protagonista.esta_vivo():
                self.final_juego(protagonista)
                return
            else:
                print("Has vencido al capitán de los esqueletos y obtenido la llave para abrir el cofre.")
                self.final_juego(protagonista,True)

        elif decision == '2':
            print("Intentas escapar de la isla sin el tesoro.")
            self.final_juego(protagonista)

juego = JuegoAventura()

juego.comenzar()



