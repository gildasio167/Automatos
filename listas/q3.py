 
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


string = input()
print (dfa(string, current, edges, accepting))