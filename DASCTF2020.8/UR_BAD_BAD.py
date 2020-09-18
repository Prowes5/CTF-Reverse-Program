# -*- coding: utf-8 -*-

cip = 'Dx0t0bDkD0NbDx0NkNNbktNkkk0txtN0kkDkxbkBxbNNBbkBDx0kDxNkD0NbDx0Nx0DBNt00'
key = '0xDktbNB'

index = []
for i in cip:
    for j in range(len(key)):
        if i == key[j]:
            index.append(j)

text = []

for i in index:
    text.append((bin(i)[2:]).zfill(3))

f = []

for i in range(0,len(text),8):
    j = 0
    tmp = ''
    while j <= 7:
        tmp += text[i+j]
        j += 1
    f.append(tmp)

flag = ''
for i in range(len(f)):
    flag += hex(int(f[i],2))[2:].decode('hex')

print flag