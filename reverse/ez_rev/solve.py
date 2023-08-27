from pwn import *

def reverse_swap(In):
    a = In[2]
    In[2] = In[13]
    In[13] = a
    a = In[3]
    In[3] = In[19]
    In[19] = a
    return In

def reverse_rev(In):
    return In[::-1]

def reverse_xor_func(In):
    In = bytearray(In)
    for i in range(len(In)):
        if (i % 3 == 2):
            In[i] = In[i] ^ 0x3e
        elif (i % 3 == 0):
            In[i] = In[i] ^ 0xff
        else:
            In[i] = In[i] ^ 0x6a
    return In

def generate_input(secret):
    input_bytes = bytearray(secret)
    input_bytes = reverse_swap(input_bytes)
    input_bytes = reverse_rev(input_bytes)
    input_bytes = reverse_xor_func(input_bytes)
    return bytes(input_bytes)

SECRET = [
0x17, 0x93, 0x91, 0x93, 0x97, 0x5d, 0x35, 0x86, 0x0d,
                          0x01, 0xa0, 0x5b, 0x19, 0x52, 0x0d, 0x09, 0xce, 0x52,
                          0x35, 0x5e, 0x0a, 0x09, 0xce, 0x4e, 0x13, 0x8b, 0x61,
                          0x18, 0x8a, 0x0e, 0x33, 0x84, 0x4d, 0x07, 0x8a, 0x57,
                          0x04, 0x9a, 0x59, 0x04, 0x96
]

input_string = generate_input(SECRET)
print(input_string)

