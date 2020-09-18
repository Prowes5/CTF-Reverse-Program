import base64

cipher = 'e3nifIH9b_C@n@dH'
flag = ''
for i in range(len(cipher)):
    flag += chr(ord(cipher[i])-i)

print base64.b64decode(flag)
