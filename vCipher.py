cipher = input("Input Cipher: ")
key = input("Input your key: ")
decode=[]
for i in range(len(cipher)):
    if(ord(cipher[i])>=ord(key[i%len(key)])):
        decode.append(chr((ord(cipher[i])-ord(key[i%(len(key))])+65)))
    else:
        decode.append(chr((ord(cipher[i])-ord(key[i%(len(key))])+91)))
print(decode)