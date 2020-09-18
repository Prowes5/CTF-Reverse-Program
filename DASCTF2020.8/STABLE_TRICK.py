# -*- coding: utf-8 -*-

input_num = [0x9A,0xCE,0xFD,0x07, \
        0x01,0x0E,0x0C,0x02, \
        0x0C,0x0D,0x24,0x2A, \
        0x24,0x26,0x24,0x22 \
        ]

def encrypt(input_num):
    sum = []
    for i in range(0,len(input_num),4):
        sum.append((input_num[i+3]<<24)+(input_num[i+2]<<16)+(input_num[i+1]<<8)+input_num[i])
    
    for k in range(1):
        tmp = k%3
        if tmp == 0:
            sum[0] = sum[0]^0x6560773b
            sum[1] = sum[1]^0xffbeadde
            
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
    
        if tmp<=1:
            sum[0] = sum[0]^0x6560773b
            sum[1] = sum[1]^0xffbeadde
            
            tmp_num = []
            for i in range(len(sum)):
                tmp_num.append(sum[i]&0xff)
                tmp_num.append((sum[i]>>8)&0xff)
                tmp_num.append((sum[i]>>16)&0xff)
                tmp_num.append((sum[i]>>24)&0xff)
    
            input_num = []
            for i in range(0,4):
                for j in range(0,4):
                    input_num.append(tmp_num[i+4*j])
            flag = 0
            flag = (sum[0]+0x6560773b)/0x100000000
            sum[0] = (sum[0]+0x6560773b)&0xffffffff
            sum[1] = (sum[1]+0xffbeadde+flag)&0xffffffff
    
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
    
        if tmp <= 2:
            flag = 0
            flag = (sum[0]+0x6560773b)/0x100000000
            sum[0] = (sum[0]+0x6560773b)&0xffffffff
            sum[1] = (sum[1]+0xffbeadde+flag)&0xffffffff
            
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
        
    for i in range(len(input_num)):
        print hex(input_num[i])

def decrypt(cip_num):
    #cip_num = [0xd8,0x78,0x7c,0xfa,0xb2,0x2c,0xe8,0xf4,0x41,0xee,0x12,0x93,0x6,0xe2,0xa2,0x2]
    tmp_num = []

    
    sum = []
    # 63
    for i in range(0,4):
        for j in range(0,4):
            tmp_num.append(cip_num[i+4*j])

    for i in range(0,len(tmp_num),4):
        sum.append((tmp_num[i+3]<<24)+(tmp_num[i+2]<<16)+(tmp_num[i+1]<<8)+tmp_num[i])
   
    sum[0] = sum[0]^0x6560773b
    sum[1] = sum[1]^0xffbeadde

    sum[0],sum[2] = sum[2],sum[0]
    sum[1],sum[3] = sum[3],sum[1]

    sum[0] = sum[0]^0x6560773b
    sum[1] = sum[1]^0xffbeadde

    # 62
    for k in range(62,-1,-1):
        tmp = k%3
        if tmp <= 2:
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
        
            flag = 0
            sum[0] = (sum[0]-0x6560773b)&0xffffffff
            flag = (sum[0]+0x6560773b)/0x100000000
            sum[1] = (sum[1]-flag-0xffbeadde)&0xffffffff
    
        if tmp <= 1:
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
        
            flag = 0
            sum[0] = (sum[0]-0x6560773b)&0xffffffff
            flag = (sum[0]+0x6560773b)/0x100000000
            sum[1] = (sum[1]-flag-0xffbeadde)&0xffffffff
        
            tmp_num = []
            for i in range(len(sum)):
                tmp_num.append(sum[i]&0xff)
                tmp_num.append((sum[i]>>8)&0xff)
                tmp_num.append((sum[i]>>16)&0xff)
                tmp_num.append((sum[i]>>24)&0xff)
        
            cip_num = []
            for i in range(0,4):
                for j in range(0,4):
                    cip_num.append(tmp_num[i+4*j])
        
            sum[0] = sum[0]^0x6560773b
            sum[1] = sum[1]^0xffbeadde
    
        if tmp == 0:
            sum[0],sum[2] = sum[2],sum[0]
            sum[1],sum[3] = sum[3],sum[1]
        
            sum[0] = sum[0]^0x6560773b
            sum[1] = sum[1]^0xffbeadde
    

    data = []
    for i in range(len(sum)):
        data.append(sum[i]&0xff)
        data.append((sum[i]>>8)&0xff)
        data.append((sum[i]>>16)&0xff)
        data.append((sum[i]>>24)&0xff)

    data += [0x65,0x60,0x77,0x3b]
    xor_decry(data)

def xor_decry(data):
    flag = ''
    flag += chr(data[0]^0xab)
    flag += chr(data[0]^data[1]^0x66)

    tmp = data[1]
    for i in range(2,5):
        t = data[i]
        data[i] ^= tmp
        flag += chr(data[i])
        tmp ^= t

    for i in range(5,10):
        t = data[i]
        data[i] ^= tmp^0xd
        flag += chr(data[i])
        tmp ^= t ^ 0xd

    for i in range(10,20):
        t = data[i]
        data[i] ^= tmp ^ 0x25
        flag += chr(data[i])
        tmp ^= t^0x25

    print flag

if __name__ == '__main__':
    #encrypt(input_num)
    cip_num = [0xae,0xd9,0xa1,0x50,0x7a,0xe1,0xf8,0xe3,0x43,0x83,0xb0,0xb0,0x17,0x9f,0xcd,0x30]
    decrypt(cip_num)
    
    
