import math
import string
string1='COOLSHELL'
string2='SHELL'
def func(fuck):
    digit=0
    for x in fuck:
        temp=ord(x)-64
        digit=digit*26+temp
    return digit
number=int(func(string1)/func(string2))           
cout=''
while(number>0):
    cout+=chr(number%26+64)
    number=number/26
print cout[::-1]
