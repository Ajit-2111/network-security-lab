from math import ceil

def removeDuplicates(text):
    textList = []
    textList[:] = text
    uniqueTextList = []
    for i in textList:
        if i not in uniqueTextList :
            uniqueTextList.append(i)
    stringSplit = ""
    return stringSplit.join(uniqueTextList)

def indexOfElementInMatrix (element,matrix):
    for i in range(0,6):
        for j in range(0,6):
            if (element == matrix[i][j]):
                cipher = adfgvxValueOfElement(i+1,j+1)
    return cipher

def adfgvxValueOfElement(elemPos_i,elemPos_j):
    position = {1: "A", 2: "D", 3: "F", 4: "G", 5: "V", 6: "X"}
    firstCipher = ""
    firstCipher += position[elemPos_i]
    firstCipher += position[elemPos_j]
    return firstCipher


plainText = input("Enter the plain text : ").replace(" ", "") # Takes plain text and removes white space
appendText = "abcdefghijklmnopqrstuvwxyz0123456789"  # tThis is to be appended to the plainText
firstKeyword = input("Enter the first keyword : ").replace(" ", "")
secondKeyword = input("Enter the second keyword : ").replace(" ", "")
newTextForMatrix = firstKeyword + appendText
uniqueText = removeDuplicates(newTextForMatrix)

uniqueTextIndex = 0
mainMatrix = []

for i in range(0,6):
    mainMatrixRow = []
    for j in range(0,6):
        mainMatrixRow.append(uniqueText[uniqueTextIndex])
        uniqueTextIndex += 1
    mainMatrix.append(mainMatrixRow)


cipher1value = ""
for i in plainText:
    cipher1value += indexOfElementInMatrix(i,mainMatrix)


if (len(cipher1value) % len(secondKeyword)) != 0:
    numOfExtraChar = len(secondKeyword)- (len(cipher1value) % len(secondKeyword))
    for i in range(numOfExtraChar):
        cipher1value += "-"

mainMatrixCipher2 = []
cipher1Index = 0
for i in range(ceil(len(cipher1value)/len(secondKeyword))):
    mainMatrixCipher2Row = []
    for j in range(len(secondKeyword)):
        mainMatrixCipher2Row.append(cipher1value[cipher1Index])
        cipher1Index += 1
    mainMatrixCipher2.append(mainMatrixCipher2Row)


secondKeywordList = list(secondKeyword)
secondKeywordList.sort()
cipher2value = ""

for i in secondKeywordList:
    elementIndex = secondKeyword.index(i)
    for j in range(len(mainMatrixCipher2)):
        cipher2value += mainMatrixCipher2[j][elementIndex]

print(cipher2value)

