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

