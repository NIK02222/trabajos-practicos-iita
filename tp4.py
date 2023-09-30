"""1)Escriba una función que muestre todos los números primos entre 1 y un número n que es 
# ingresado por parámetro"""

# def es_primo(num):
#     if num <= 1:
#         return False
#     elif num <= 3:
#         return True
#     elif num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def numeros_primos_hasta_n(n):
#     primos = []
#     for numero in range(2, n + 1):
#         if es_primo(numero):
#             primos.append(numero)
#     return primos

# # Para probar la función con n = 20, por ejemplo:
# n = 20
# print("Números primos entre 1 y", n, "son:", numeros_primos_hasta_n(n))

"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta 
que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje 
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del 
programa de acuerdo a estos criterios: 
• Use un test condicional en el ciclo while para detener la ejecución. 
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""

"""*Versión 1: Usando un test condicional en el ciclo while para detener la ejecución:*"""

# def hacer_sandwich():
#     condimentos = []
#     condimento = input("Ingresa un condimento para el sándwich o escribe 'salir' para terminar: ")
    
#     while condimento != 'salir':
#         condimentos.append(condimento)
#         print("Se ha agregado", condimento, "al sándwich.")
#         condimento = input("Ingresa otro condimento o escribe 'salir' para terminar: ")
    
#     print("Los condimentos en tu sándwich son:")
#     for ingrediente in condimentos:
#         print(ingrediente)

# hacer_sandwich()
"""Versión 2: Usando un test condicional dentro del ciclo para decidir si continuar la ejecución:*"""

# def hacer_sandwich():
#     condimentos = []
#     while True:
#         condimento = input("Ingresa un condimento para el sándwich o escribe 'salir' para terminar: ")
        
#         if condimento == 'salir':
#             break
        
#         condimentos.append(condimento)
#         print("Se ha agregado", condimento, "al sándwich.")
    
#     print("Los condimentos en tu sándwich son:", ", ".join(condimentos))

# hacer_sandwich()

"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un 
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez 
usando argumentos por posición. Llámela una segunda vez usando argumentos por clave. 
B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por 
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los 
valores por defecto, y la segunda con valores diferentes. """
#A) Aquí tienes la función `hacer_remera()` y las llamadas a la función utilizando argumentos por posición y por clave:
# def hacer_remera(tamaño, mensaje):
#     print("Tamaño de la remera:", tamaño)
#     print("Mensaje impreso en la remera:", mensaje)

# # Llamada utilizando argumentos por posición
# hacer_remera("M", "Hola Mundo")

# # Llamada utilizando argumentos por clave
# hacer_remera(mensaje="Python Rocks!", tamaño="S")

# """B) Ahora, modificaremos la función `hacer_remera()` para que tenga valores por defecto para el tamaño y el mensaje, y luego crearemos un par de remeras, una con los valores por defecto y otra con valores personalizados:"""
# def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
#     print("Tamaño de la remera:", tamaño)
#     print("Mensaje impreso en la remera:", mensaje)

# # Remera con valores por defecto
# hacer_remera()

# # Remera con valores personalizados
# hacer_remera(tamaño='M', mensaje='Hello World')
"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)."""
def fibonacci(n):
    # Inicializamos la lista de Fibonacci con los dos primeros números
    fib_sequence = [0, 1]
    
    # Generamos los números restantes de la serie de Fibonacci
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Ejemplo de uso: obtener los primeros 10 números de la serie de Fibonacci
n = 10
resultado = fibonacci(n)
print(resultado)