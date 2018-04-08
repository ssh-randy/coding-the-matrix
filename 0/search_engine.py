def makeInverseIndex(strlist):
    inverseIndex = {}
    docs = enumerate(strlist)
    for docNum, doc in docs:
        listOfWords = doc.split()
        for word in listOfWords:
            if word in inverseIndex:
                inverseIndex.get(word).add(docNum)
            else:
                docSet = {docNum}
                inverseIndex[word]=docSet
    return inverseIndex

                
                

def orSearch(inverseIndex, query):
    containingDocs = set()

    for word in query:
        if word in inverseIndex:
            containingDocs = containingDocs | inverseIndex[word]

    return containingDocs

def andSearch(inverseIndex, query):
    containingDocsList = []

    for word in query:
        if word in inverseIndex:
            containingDocsList.append(inverseIndex[word])

    return set.intersection(*containingDocsList)

    
