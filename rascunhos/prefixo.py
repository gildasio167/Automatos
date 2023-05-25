def palavra(w, Σ):
  if w == "":
    return True
  else:
    a = w[0]
    x = w[1:]

    if a in Σ and palavra(x, Σ):
      return True
    else:
      return False

palavra("abbbd", "abc")