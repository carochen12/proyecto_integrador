resultados = []

def mostrar_menu():
    print("JUEGO PIEDRA, PAPEL O TIJERA")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")

def jugar():
    mostrar_menu()
    
    jugador1 = int(input("Jugador 1, elija: "))
    jugador2 = int(input("Jugador 2, elija: "))

    if jugador1 == jugador2:
        resultado = "Empate"
    elif (jugador1 == 1 and jugador2 == 3) or \
         (jugador1 == 2 and jugador2 == 1) or \
         (jugador1 == 3 and jugador2 == 2):
        resultado = "Gana Jugador 1"
    else:
        resultado = "Gana Jugador 2"

    print("Resultado: ", resultado)
    resultados.append(resultado)


while True:
    jugar()
    
    continuar = input("Desea jugar otra vez? (s/n): ")
    if continuar.lower() != "s":
        break


print("RESULTADOS FINALES")
print("Partidas jugadas: ", len(resultados))
print("Resultados: ", resultados)
print("Gracias por jugar")
