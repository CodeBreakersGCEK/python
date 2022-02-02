# -------------------------------TUT-1- Variables in Python-----------------------------------------#

# print("Python") # as the name suggested it's a function which is used to  print a python  objects .

# Variables - Basically variable is a container where you can put your value
# x=2 # Here x is the container and 2 is the value
# print(x)



# Why it's called  variables ? -- Bcz we can change its value ..
# intigers
# x=3
# print(x)

# we dont need to decalre any type of variable



# Strings - These are combinations of Character
name="Python"
# print(name)
# print(name*2)

# As we said that Strings are combination of Character,Now the question arise can we fetch the character ?
# print(name[0])
# print(name[3])
# print(name[6]) # Show error string index out of range

# we can also used negative numbers while fetching
# when we use negative number its start from ending
# name="Python"
# print(name[-1])


# fetching two character
name="Python"
# print(name[0:2])
# print(name[1:4])
# print(name[1:])
# print(name[:4])
# print(name[:3])


name="Python"

name[0]="C" # Throw Error
print(name) # 'str' object does not support item assignment i.e string is immutable

# counting Character in sting
# name="Python"
print(len(name))

#------------------------------------------------------Tut-2- SET and Operation on set-------------------------------------

# In Python List are the collection of data,maybe similar type or may not be

list=[1,2,3,4,5,6,7,8,9] # List in mutable
list[0]=11 # Here "0" replace "1"
print(list)
# print(list[0])
# print(list[1])
# print(list[-1])

list1=["C","C++","Java","Go","HTML","Python","Cython","Z"]
# print(list1)




list2=[99,78,"Java",90,"JavaScript"]
# print(list2)


# we can also make list of list

# list3=[list,list1,list2]
# print(list3)


# Some Operations on list
list=[1,2,3,4,5,6,7,8,9]


# Append - In append the assignment was done at the end
# list.append(10)
# print(list)

# insert
# list=[1,2,3,4,5,6,7,8,9]
# list.insert(2,77)
# print(list)

#extend- used to add multiple value
# list=[1,2,3,4,5,6,7,8,9]
# list.extend([7,77,777,90909,3,45])
# print(list)






# remove - remove by value
# list=[1,2,3,4,5,6,7,8,9]
# list.remove(7)
# print(list)

#pop-remove by index

# list=[1,2,3,4,5,6,7,8,9]
# list.pop(1)
# print(list)



# min-find minimum value

# list2=[99,78,"Java",90,"JavaScript"]
# a=min(list2) # Throw error
# print(a)

#min-find maximum value

# list2=[99,78,"Java",90,"JavaScript"]
# a=max(list2)
# print(a)

#sum
# list=[1,2,3,4,5,6,7,8,9]
# b=sum(list)
# print(b)

#sort
list4=[1,2,3,4,5,6,7,8]

a=list4.count(9)
print(a)



# list4.sort()
#
# print(list4)
# list4.sort(reverse=True)
# #
# print(list4)

#------------------------------------------------------Tut-3- Dictionary and Operation on set-------------------------------------
# Dictionary is nothing but key value pairs

#Class Dictionary
# d1={1,2,3,4}
# print(type(d1))

#Class List
# d1=[]
# print(type(d1))

#Class Tuple
# d1=()
# print(type(d1))

d2={"Ram":"Ice Cream",
    "Shayam":"Momo",
    "Saswat":" Chicken Pokoda",

    "Jitu":"Chicken 65",
    "Sasmita":{"B":"bread","L":"Rice","D":"Roti"}}  #Key Values may be A Dictionary
                                                   # May be a list and May be tuple


# Adding Items
d2["Sai"]="Cake"
d2["Harish"]="Cold Drink"

# print(d2)

# Removing Items
del d2["Harish"]
# print(d2)

d3=d2
# print(d3)
# del d3["Ram"] #As we see If we delet "Ram" in d3 , "Ram" d2 also deleted so use copy function
# print(d2)

#Copy Function

d3=d2.copy()
del d3["Ram"]
# print(d2) #"Ram" Deleted in d3 not in d2
# print(d3)

# get function
# print(d2.get("Shayam"))

#update Function
d2.update({"Rohan":"Chips"})
# print(d2)

# If you want to print all Keys in a Dictionary
# print(d2.keys())

# If you want to print all items in a Dictionary
print(d2.items())


#------------------------------------------------------Tut-4- Loops in Python -------------------------------------

# ForLoop in Python


# for i in range(0,11):
#     print(f"The itrative numbers are {x} ")
#     x=x+1
print("Hello",end=" ")
x=0
while x<100:
   print(x,end="  ")
   x=x+1

#Example in List

# List1=["C","C++","Python","Go","JS"]
# for item in List1:  ##This is the Process of Iteration. It can be done by List
#     print(item)

#Example in Tuple

# Tup1=("Avk","Bvk","Cvk","Dvk")
# for item in Tup1: ##This is the Process of Iteration. It can be done by Tuple
#    print(item)

#Using Loop in List of List

List1=[["Shyam","65"],["Rohan","78"],["Hasrish","90"],["Rasid","23"]]
# for name,lang in List1:
#     print(f"The student's name is {name} and his familar language is  - {lang}")  # Its also can be done tuple

#Example of for loop in Dictionary
List1=[["Shyam","65"],["Rohan","78"],["Hasrish","90"],["Rasid","23"]]
dict1=dict(List1)  ##This is the method add list in Dictionary
# print(dict1)
# for name,weight in dict1.items():  ## Fro loop in Dictionary is quite different as compare to list and tuple here (.items()) function is used
#   print(name," and his weight is - ",weight,"Kg")

#If you want print only key in Dictionary you can use this as shown in below --

# for item in dict1:
#      print(item)


                                         #Quiz
# List2=[int,1.29,True,"Avk","BVL","XYZ",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for item in List2:
#     if str(item).isnumeric() and item<=9 in List2 :  ##Remeber if the list is mixed with string and numbers must use {isnumeric()} function
#         print(item)




# Printing Pattern

# Pattern 1- Pyramid Pattern

# n=int(input("Enter no of rows that you want to print"))
# # here i is for row and j is for column
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

# Pattern 2- Reverse Pyramid Pattern

# n=int(input("Enter no of rows that you want to print"))
# for i in range(n+1,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# Pattern 3- Row number Pattern

# n=int(input("Enter no of rows that you want to print"))
# # here i is for row and j is for column
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")

    # Res
    # 1
    # 2 2
    # 3 3 3
    # 4 4 4 4
    # 5 5 5 5 5


# Pattern 3- Column number Pattern

# n = int(input("Enter no of rows that you want to print"))
# # here i is for row and j is for column
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i,j, end=" ")
#     print("")

#------------------------------------------------------Tut-5- -------------------------------------

## Operators in Pyhthon

## Arithmetic Operator
## Assignment Operator
## Comparison Operator
## Logical  Operator
## Identity Operator
## Membership Operator
## Bitwise Operator

##  Arithmetic Operator
# print("7+8 is - ",7+8)
# print("7-8 is - ",7-8)
# print("7*8 is - ",7*8)
# print("2**4 is - ",2**4) # 2 multiply by 2 ,3 times
# print("17/8 is - ",17/8)
# print("17//8 is - ",17//8) #floor division Operator
#                         # In this operator the result is came in Intiger Value
# print("22 % 3 is - ",22%3) #  Modulo Operator
#                            # In this opertor gives the Reminder

## Assignment Operator

# x=5
# # print(x)
# x+=7
#
# print(x)

## Comparison Operator

# i=5
# print(i != 5)

## Logical  Operator

# a=False
# b=False
# print(a and b)
# print(a or b)


## Identity Operator

# print(5 is not 5)

## Membership Operator

# list1=[1,3,56,78,7,32,99,8]
# print(78 in list1) #If the Element is Present its return True else False
# print(78 not in list1)

## Bitwise Operator


# 1 - 01
# 0 - 00

# 0 - 00
# 2 - 10
# 3 - 11

print(2 & 3)
print(2 | 3)

#------------------------------------------------------Tut-6-Short hand if else-------------------------------------


# a=int(input("Enter a 1st number\n"))
# b=int(input("Enter a 2nd number\n"))
#
# if a>b:
#     print(f"{a} is greater")
# elif b>a :
#     print(f"{b} is gretaer")
#
# else:
#     print("equal")


##Shorthand If else
#
"""
ihisfkaf[ogwikfsdfdojfisdvdvdfv
ksjdgisdjgosdkgpf[
"""
a=int(input("Enter a 1st number\n"))
b=int(input("Enter a 2nd number\n"))
print("2nd number is greater than 1st") if a<b else print("1st number is greater than 2nd")
## Here the if is for 1st statement and else is for 2nd statement

