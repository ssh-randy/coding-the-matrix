def makeInverseIndex(strlist):
  inverseIndex = {}
  documentAndIndex = list(enumerate(strlist))
  for (index, document) in documentAndIndex:
    wordList = document.split()
    for word in wordList:
      if word not in inverseIndex:
        inverseIndex[word] = set([index])
      else:
        inverseIndex[word].add(index)
  return inverseIndex


def orSearch(inverseIndex, query):
  resultSet = set()
  for word in query:
    resultSet.update(inverseIndex[word])
  return resultSet

def andSearch(inverseIndex, query):
  listOfSets = []
  for word in query:
    listOfSets.append(inverseIndex[word])
  return set.intersection(*listOfSets)
  
