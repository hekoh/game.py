from random import choice, randrange
from datetime import datetime
operators = ["+", "-","*","/"]
times = 5
init_time = datetime.now()
correctas = 0
incorrectas = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    if operator == "+":
            resultado = str (number_1 + number_2)
    elif operator == "-":
            resultado = str (number_1 - number_2)
    elif operator ==  "*":
            resultado = str (number_1 * number_2)
    elif operator == "/":
            resultado = str (number_1 / number_2)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = input("resultado: ")
    print(result)
    if result == resultado:
        print('respuesta correcta!')
        correctas = correctas + 1 
        print(correctas)
    else:
        print('respuesta incorrecta!, el resultado era: ',resultado)
        incorrectas = incorrectas + 1
end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.") 
print(f"la cantidad de respuestas correctas fue de: {correctas} y la cantidad de fallos fue de: {incorrectas}")