

def isNumber(n):
  try:
    float(n)
    return True
  except ValueError:
    return False

def isOperator(o):
  return o in ["+","-","*","/"]


def continuar(e):
  if e.upper() == "Y":
    return True
  else:
    return False

def userExists(user,df):
    return user in df['usuario'].values
