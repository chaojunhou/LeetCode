#coding=utf8
import string
def func(obj):
    hou=[0 for x in range(255)]
    for i in range(len(obj)):
        hou[ord(obj[i])]+=1
    for i in range(len(obj)):
            if hou[ord(obj[i])]==1:
                print 'the first number in the string is:'+ obj[i]
                break
func("houchao")
            
    
