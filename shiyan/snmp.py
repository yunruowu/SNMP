s = ''
b = '0X536f66747761'


x = '0x57414e204d696e69706f727420284c3254502900'
i=len(x)
y = bytearray.fromhex(x[2:i-2])
z = str(y)
# def hex_to_str(s):
#     return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])
j = len(z)
print(z[11:j-1])