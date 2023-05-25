# Strings binárias que começam ou terminam com 01
edges = { 
    (0,'') : [1,4],
    (1,'0') : [2],
    (1,'1') : [5],
    (2,'0') : [3],
    (2,'1') : [5],
    (3,'0') : [3],
    (3,'1') : [3],
    (4,'1') : [5],
    (5,'0') : [5],
    (5,'1') : [6],
    (6,'0') : [6]

 }
initial   = 0
accepting = [3,6] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False

import random

def generate_random_binary():
    while True:
        binary = bin(random.randint(1, 15))[2:]  # Gera um número aleatório entre 1 e 1000 e converte para binário
        count_zeros = binary.count('0')  # Conta o número de '0' no número binário
        count_ones = binary.count('1')  # Conta o número de '1' no número binário
        
        if count_zeros >= 2 or count_ones == 2:
            return binary


string = generate_random_binary()
print(string)
print (epsilon_nfa( string , initial, edges, accepting) )      