# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [2,1],
          (1,'1') : [3], 
          (2,'0') : [7],
          (7,'0') : [7],
          (7,'1') : [3],
          (3,'0') : [8],
          (3,'1') : [4],
          (4,'0') : [5],
          (8,'0') : [9],
          (8,'1') : [5],
          (9,'0') : [10],
          (9,'1') : [6],
          (4,'1') : [5],
          (5,'0') : [6],
          (5,'1') : [6],
          (6,'0') : [3],
          (6,'1') : [3],
          (10,'1'): [3]
 }
initial   = 0
accepting = [3, 4, 5, 6, 8, 9, 10] 

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