edges = {
    (0, 'a'): [1],
    (0, 'b'): [0],
    (1, 'b'): [2],
    (2, 'a'): [3],
    (3, 'b'): [8],
    (2, 'b'): [4],
    (4, 'a'): [5],
    (4, 'b'): [4],
    (5, 'a'): [6],
    (6, 'b'): [7],
    (8, 'b'): [9],
    (9, 'a'): [10]
    
}

current = 0
accepting = [3, 5, 7]

def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstates = edges[(current, letter)]
            for state in newstates:
                if dfa(remainder, state, edges, accepting):
                    return True
        return False

string = input()
print(dfa(string, current, edges, accepting))
