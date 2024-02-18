def esPalindromo(palabra):
    palabra = eliminarEspaciosBlanco(palabra)
    size = len(palabra) -1
    palReverse = reverse(palabra, size)
    return palabra == palReverse


def eliminarEspaciosBlanco(palabra):
    return palabra.lower().replace(" ","")


def reverse(palabra, size):
    palReverse = ""
    for _ in palabra:
        palReverse += palabra[size]
        size -=1
    return palReverse









palabra = input("Digame una palabra y te dire si es palindromo o no: ")
result = "es un palindromo" if esPalindromo(palabra) else "no es un palindromo"

print(f"La palabra {palabra} {result}")