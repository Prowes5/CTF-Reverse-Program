cipher = [180, 136, 137, 147, 191, 137, 147, 191, 148, 136, 133, 191, 134, 140, 129, 135, 191,65]
flag = ''
for i in range(len(cipher)):
    flag += chr(cipher[i]-ord('@')^0x20)
print flag