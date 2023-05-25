# Strings binárias que começam ou terminam com 01
edges = { 
    (0,'') : [1,4],
    (1,'0') : [2],
    (1,'1') : [5],
    (2,'0') : [3],
    (2,'1') : [6],
    (3,'0') : [3],
    (3,'1') : [3],
    (4,'1') : [5],
    (5,'0') : [2],
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
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )      