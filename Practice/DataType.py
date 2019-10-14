import math
import cmath

#int float
a = 20
a1 = 0xAE
b = 32.6
c = int(b)  #32
d = round(b) #33
e = str(b)
f = float(a)
g = pow(a,2)
h = math.sqrt(4)
i = cmath.sqrt(-1)
j = math.floor(b) #32
k = math.ceil(b)  #33
print (a,a1,b,c,d,e,f,g,h,i,j,k)

#string
print ("Hello World")
print ("Hello\nWorld")
print (repr("Hello\nWorld"))

print('''Test one
Test two
Test three''')
print('C:\\Program Files\\fnord\\foo\\bar\\baz\\frozz\\bozz')
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')


#unicode
print("\u00c6")
print("\U0001F60A")
print("This is a cat: \N{Cat}  This is a Bus: \N{Bus}")
print("\u0001F647")
print("\U0001F647")
print(b'Hello World')
print('Hello World'.encode("ASCII"))
print('Hello World'.encode("UTF-8"))
print('Hello World'.encode("UTF-32"))
