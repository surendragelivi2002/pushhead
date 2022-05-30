'''#1  operators
arr=[2,4,5,6,3,55,3,8]
x=int(input("enter integer element"))
if x in arr:
   print("exists")
if x not in arr:
   print("notexists")


  #2
name=input("enter name")
age=int(input("enter age"))
currentyear=int(input("enter present year"))
ye=100-age
presentyear=currentyear+ye
print("you will cross age 100 by",presentyear)


#3
radius=int(input("enter radiusvalue"))
height=int(input("enter height value"))
v=(3.14*(radius**2)*height)/3
print("volume of cone is",v)

#4
from math import *
x1=int(input("enter x1value"))
x2=int(input("enter x2value"))
y1=int(input("enter y1value"))
y2=int(input("enter y2value"))
dis=sqrt((x2-x1)**2+(y2-y1)**2)
print("distance betweentwo points is ",dis)

#5 control structure

email=input("enter email")
print(email)
v=['a','e','i','o','u']
vc=0
cc=0
di=0
sp=0
for i in email:
    if i in "aeiouAEIOU":
       vc+=1
    elif i in "0123456789":
        di+=1
    elif i.isspace():
        sp+=1
    else:
        cc+=1
print("no of vowels",vc)
print("no of consonants",cc)
print("no of digits",di)
print("no of spaces",sp)


#6
d={'true':'false','bye':'goodbye','good':'bad'}
val=input("enter value")
for key,value in d.items():
    if key==val:
       print(value)
    
        

#7
num=5
def sumOfSeries(num):
    res = 0
    fact = 1
    for i in range(1, num+1):
        fact *= i
        res = res + (i/ fact)
    return res
print("Sum: ", sumOfSeries(num))
 

#8 lists
l=[55,45,33,54,88]
for i in l:
    if i%4==0 and i%5!=0:
        print(i)


#9
l=[23,10,15,14,63]
oc=0
ec=0
for i in l:
    if i%2==0:
        ec+=i
    else:
        oc+=i
print(oc,ec)



#10
l=[23,10,15,14,63]
for i in range(len(l)):
    if i%2==1:
       print(l[i])


#11
l=[23,10,15,14,63]
ll=[]
for i in l:
    if i not in ll:
        ll.append(i)
print(ll)


'''








































