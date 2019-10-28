from math import *
from string import Template
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
print(repr("Hello\nWorld"))  # 'Hello\nWorld'

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


#string format
format = "Hello, %s. %s enough for ya?"  # Hello, world. Hot enough for ya?
values = ('world', 'Hot')
print(format % values)

tmpl = Template("Hello, $who! $what enough for ya?")
tmpl.substitute(who="Mars", what="Dusty")

# first, second and third
print("{}, {} and {}".format("first", "second", "third"))
# first, second and third
print("{0}, {1} and {2}".format("first", "second", "third"))
#to be or not to be
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")) 
# π is approximately 3.14.
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
# π is approximately 3.141592653589793.

print("{name} is approximately {value}.".format(value=pi, name="π"))
# Euler's constant is roughly 32.6.
print(f"Euler's constant is roughly {e}.") 

print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))  # 3 1 4 2
print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))  # 3 2 4 1

fullname = ["Alfred", "Smoketoomuch"]  
print("Mr {name[1]}".format(name=fullname))  # Mr Smoketoomuch


tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
# The math module defines the value 3.141592653589793 for π
print(tmpl.format(mod=math))
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))  # （s、r和a）指定分别使用str、repr和ascii进行转换
print("The number is {num:b}".format(num=42))  # 'The number is 101010'
print("{num:10}".format(num=3))  # 3
print("{name:10}".format(name="Bob"))  # Bob
print("Pi day is {pi:.2f}".format(pi=pi))  # Pi day is 3.14
print("{pi:10.2f}".format(pi=pi))  # 3.14
print('One googol is {:,}'.format(10**100))
print('{:010.2f}'.format(pi))  # 0000003.14
print(print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi)))
print("{:$^15}".format(" WIN BIG "))  # '$$$ WIN BIG $$$'


#===================================
#Item                          Price
#-----------------------------------
#Apples                         0.40
#Pears                          0.50
#Cantaloupes                    1.92
#Dried Apricots(16 oz.)         8.00
#Prunes(4 lbs.)                12.00

width = 35
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

#*****The Middle by Jimmy Eat World*****
print("The Middle by Jimmy Eat World".center(39, "*"))

title = "Monty Python's Flying Circus"
print(title.find('Python'))
print(title.index('Python'))
