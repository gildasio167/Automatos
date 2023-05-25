#def prefixo(x, y):
#    if x == "":
#        return True
#    else: 
#        a = x[0]
#        b = x[1:]

#        if a in y and prefixo(b, y):
#            return True
#        else:
#            return False


def prefixo(w, Σ):
  if w == "":
    return True
  else:
    a = w[0]
    x = w[1:]

    if a in Σ and prefixo(x, Σ):
      return True
    else:
      return False

def main():
    x = input()
    y = input()
    print( prefixo(x,y) )



