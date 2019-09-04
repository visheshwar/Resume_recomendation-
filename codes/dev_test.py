
from autocorrect import spell
Final_Array = []
def lcs(X, Y):
    try:
        mat = []
        for i in range(0,len(X)):
            row = []
            for j in range(0,len(Y)):
                if X[i] == Y[j]:
                    if i == 0 or j == 0:
                        row.append(1)
                    else:
                        val = 1 + int( mat[i-1][j-1] )
                        row.append(val)
                else:
                    row.append(0)
            mat.append(row)
        new_mat = []
        for r in  mat:
            r.sort()
            r.reverse()
            new_mat.append(r)
        lcs = 0
        for r in new_mat:
            if lcs < r[0]:
                lcs = r[0]
        return lcs
    except:
        return -9999
        
def spellCorrect(string):
    words = string.split(" ")
    correctWords = []
    for i in words:
        correctWords.append(spell(i))
    return " ".join(correctWords)

def semanticSearch(searchString, searchSentencesList):
    result = None
    searchString = spellCorrect(searchString)
    bestScore = 0
    for i in searchSentencesList:
        score = lcs(searchString, i)
        print(score , i[0:100])
        print("")
        temp = [score]
        Final_Array.extend(temp)
        if score > bestScore:
            bestScore = score
            result = i
    return result


print(semanticSearch('tasty', ['delicious','sweet','stale','horrible', 'tasty']))
