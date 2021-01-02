

def my_filter(L, num):
  return [x for x in L if x%num!=0]

def my_lists(L):
  return [[x+1 for x in range(listElement)] for listElement in L]

def my_function_composition(f,g):
  return {(k,g[v]) for k,v in f.items()}

def mySum(L):
  current = 0
  for item in L:
    current+=item
  return current

def myProduct(L):
  current = 1
  for item in L:
    current*=item
  return current

def myMin(L):
  localMin = None
  for item in L:
    if localMin is None:
      localMin = item
    if item < localMin:
      localMin = item
  return localMin

def myConcat(L):
  concatStr = ''
  for str in L:
    concatStr += str
  return concatStr

def myUnion(L):
  unionOfSets = set()
  for subSet in L:
    unionOfSets.update(subSet)
  return unionOfSets

def transform(a,b,L):
  return [a*z + b for z in L]
