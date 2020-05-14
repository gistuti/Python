'''Q1.

a)
number=int(input("enter the number:"))
count=0
while(number > 0):
    number=number//10
    count +=1
print("number of digits are: %d" %count)


b)     

list1=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
    elements=int(input())
    list1.append(elements)
print(list1)
for i in range(len(list1)-1,-1,-1):
    print(list1[i])


Q2.

s1=input("enter string")
s2=input("enter string")

def appendedString(s1, s2):
    mid=int(len(s1)/2)
    print("strings are:",s1,s2)
    resultString= s1[:mid-1:]+s2+s1[mid-1:]
    print("resultant string:", resultString)

Q3.

input_string=input("enter the string:" )
uppercase=[]
lowercase=[]

for i in input_string:
    if i.isupper():
        uppercase.append(i)
    else:
        lowercase.append(i)
result=''.join(lowercase+uppercase)
print(result)


Q5.

list1=[]
n=int(input("list1 number of elements:"))
for i in range(0,n):
    elements=int(input())
    list1.append(elements)
print(list1)

list2=[]
n=int(input("list2 number of elements:"))
for i in range(0,n):
    elements=int(input())
    list2.append(elements)
print(list2)

'''

list3=[]

odd=list1[1::2]
print(odd)

even=list2[0::2]
print(even)

list3.extend(odd)
list3.extend(even)
print(list3)
    

