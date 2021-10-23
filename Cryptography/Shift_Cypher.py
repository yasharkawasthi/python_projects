c = input('Enter the ciphered text: ')
c = c.upper()
k = int(input('Enter the Key: '))
t = 0
p = ''
for char in c:
    j = ord (char)
    h = j-k
    if h < 65:
        u = 91 - (65 - h)
    else:
        u = h
    b = chr(u)
    p = p+b
print ("Plain text :")
print (p)
