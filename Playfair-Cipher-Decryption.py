def removeDuplicates(text):
    textList = list(text)
    uniqueTextList = []
    for i in textList:
        if i not in uniqueTextList :
            uniqueTextList.append(i)
    stringSplit = ""
    return stringSplit.join(uniqueTextList)

def keySquareMatrix(key):
    appendText = "abcdefghijklmnopqrstuvwxyz"  # This is to be appended to the plainText
    matrixText = removeDuplicates(key+appendText)
    if (matrixText.index("i") < matrixText.index("j")):
        uniqueText = matrixText.replace("j", "")
    else:
        uniqueText = matrixText.replace("i","").replace("j","i")
    uniqueTextIndex = 0
    mainMatrix = []
    for i in range(0, 5):
        mainMatrixRow = []
        for j in range(0, 5):
            mainMatrixRow.append(uniqueText[uniqueTextIndex])
            uniqueTextIndex += 1
        mainMatrix.append(mainMatrixRow)
    return mainMatrix

def indexofelement(char,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if char == matrix[i][j]:
                return [i,j]

def decipher(cipher,matrix):
    plainText = []
    for i in range(0, len(cipher), 2):
        text = cipher[i:i+2]
        firstchar = text[0]
        secondchar = text[1]
        firstcharindex = indexofelement(firstchar,matrix)
        secondcharindex = indexofelement(secondchar,matrix)
        if firstcharindex[0] == secondcharindex[0]:
            if firstcharindex[1]==0:
                plainText.append(matrix[firstcharindex[0]][4])
                plainText.append(matrix[secondcharindex[0]][secondcharindex[1]-1])
            elif secondcharindex[1]==0:
                plainText.append(matrix[firstcharindex[0]][firstcharindex[1]-1])
                plainText.append(matrix[secondcharindex[0]][4])
            else:
                plainText.append(matrix[firstcharindex[0]][firstcharindex[1] - 1])
                plainText.append(matrix[secondcharindex[0]][secondcharindex[1] - 1])
        elif firstcharindex[1] == secondcharindex[1]:
            if firstcharindex[0]==0:
                plainText.append(matrix[4][firstcharindex[1]])
                plainText.append(matrix[secondcharindex[0] - 1][secondcharindex[1]])
            elif secondcharindex[0] == 0:
                plainText.append(matrix[firstcharindex[0] - 1][firstcharindex[1]])
                plainText.append(matrix[4][secondcharindex[1]])
            else:
                plainText.append(matrix[firstcharindex[0] - 1][firstcharindex[1]])
                plainText.append(matrix[secondcharindex[0] - 1][secondcharindex[1]])
        else:
            plainText.append(matrix[firstcharindex[0]][secondcharindex[1]])
            plainText.append(matrix[secondcharindex[0]][firstcharindex[1]])
    return plainText

inputCipher = input("Enter the cipher text : ")
cipherText =  inputCipher.lower()
inputKeyword = input("Enter the keyword : ")
keyword = removeDuplicates(inputKeyword.lower())
squarematrix = keySquareMatrix(keyword)
decipherlist = decipher(cipherText,squarematrix)
originaltext = ""
for i in decipherlist:
    originaltext += i
print(originaltext.replace("x",""))




