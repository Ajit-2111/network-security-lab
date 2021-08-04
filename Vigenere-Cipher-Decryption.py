def vigenereDecrypt(cipher,keyword):
    if len(keyword) != len(cipher):
        keyword = keyword*(len(cipher)%len(keyword)) #repeat keyword to approx match cipher length
        keyword = keyword[0:len(cipher)]  #make len(cipher) == len(keyword)
    plaintext = ""
    for i in range(len(cipher)):
        alp = "abcdefghijklmnopqrstuvwxyz"
        ei = alp.index(cipher[i])
        ki = alp.index(keyword[i])
        plaintext += alp[(ei - ki + 26) % 26]
    return plaintext

inputCipher = input("Enter the Cipher Text : ").lower()
inputKeyword = input("Enter the Keyword : ").lower()
result = vigenereDecrypt(inputCipher,inputKeyword)
print(result)
