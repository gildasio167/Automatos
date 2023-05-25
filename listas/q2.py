#Código Python 
# Automato que aceita string binarias com a substring 01
# 
#   
edges = { # função de transição
(1, '0') : 3,
(1, '1') : 2,
(2, '1') : 1,
(2, '0') : 3,
(3, '0') : 2,
(3, '1') : 4,
(4, '0') : 3,
(4, '1') : 5,
(5, '0') : 6,
(5, '1') : 7,
(6, '0') : 7,
(6, '1') : 7,
(7, '0') : 6,
(7, '1') : 6      
}

current = 1 # estado inicial
accepting = [5, 6, 7] # estados finais

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