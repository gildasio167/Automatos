 
edges = { # função de transição
     (1, '1') : 2,
    (2, '0') : 3,
    (2, '1') : 6,
    (3, '0') : 7,
    (3, '1') : 4,
    (7, '1') : 4,
    (7, '0') : 3,
    (4, '0') : 4,
    (4, '1') : 2,
    (5, '0') : 5,
    (5, '1') : 2,
    (6, '1') : 4,
    (6, '0') : 6

       
}

current = 1 # estado inicial
accepting = [4, 5, 6] # estados finais

import random

def generate_random_multiple_of_5():
    number = random.randint(1, 5000)  # Gera um número aleatório entre 1 e 1000
    
    if number % 5 != 0:
        # Se o número não for múltiplo de 5, encontra o próximo múltiplo de 5
        number = number + (5 - (number % 5))

    binary = bin(number)[2:]  # Converte o número para binário
    return binary


# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = generate_random_multiple_of_5()
print(string)
print (dfa(string, current, edges, accepting))
