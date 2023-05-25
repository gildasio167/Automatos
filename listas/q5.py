# Exemplo de NFA que aceita as strings binárias com o penúltimo dígito igual a 1
edges = {  (1,'0') : [2],
           (1,'1') : [4],
           (2,'1') : [4],
           (2,'0') : [3],
           (3,'0') : [3],
           (3,'1') : [4],
           (4,'1') : [5],
           (4,'0') : [2],
           (5,'1') : [5],
           (5,'0') : [2] 
}
initial   =  1 # estado inicial
accepting = [3, 5] # conjunto de estado final

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )