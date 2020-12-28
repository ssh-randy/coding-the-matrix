# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[keylist[i]] for i in range(len(keylist))]

def list2dict(L, keylist):  return {key:value for (key,value) in list(zip(keylist,L))}

def listrange2dict(L): return {i:L[i] for i in range(len(L))}
