def fibonnaci (n):
  if n <= 1:
     return n
  return fibonnaci(n-1) + fibonnaci(n-2)

def lucas (n):
  if n == 2:
    return 1
  if  n == 1:
    return 2
  return lucas (n-1) + lucas (n-2)

def sum_series (n, a=0, b=1):
  if n ==2:
    return b
  if n == 1:
    return a
  return sum_series (n-1,a,b) + sum_series(n-2,a,b)