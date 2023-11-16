cipher = input("Input Cipher: ")
key = input("Input your key: ")
decode=[]
for i in range(len(cipher)):
    decode.append(chr(ord(cipher[i])+(65-ord(key[i%len(key)]))))
print(decode)