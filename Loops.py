# Loops: used for repeating instructions.
# 2 types: While loop & For loop. They are the key words.
'''
# While loop:
# Print hello for 5 times.

count=1    # count is known as iterator
while count <=5:
    print("hello")
    count +=1        # Increase the counter by 1.

print(count) # count=6

# Break and continue key words:

# Break: used to terminate the loop when encountered.
i=1
while i <=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")

# Continue: acts as skip, terminates the execution in the current iteration and continues execution of the loop with next iteration.
i=1
while i <=5:
    if(i==3):   #checks if i==3 (3 must no to be printed is our aim)
        i+=1    # increaments the i value.
        continue  #do not print as we want to skip the value to be printed
    print(i)
    i+=1
print("end of loop")

# print only even numbers using loop (continue keyword)

i=1
while i <= 10:
    if(i%2 != 0):  #skipping all odd numbers
        i +=1
        continue
    print(i)
    i +=1
print("end of code")

# For: Loops are used for sequential traversal. For traversing lists, strings, tuples etc. No need of indexcing.
# if printed, if prints in the sequential order.

list=[10,20, "potato", "brinjal", "ladyfinger"]

for el in list:
    print(el)

# print each alphabet in the string.
str1="Rama Pulagam"
for char in str1:      #char is each alphabet
    print(char) #will print my name

# For loop with else
str2= "apna college"
for char in str2:
    if(char=='r'): #string type
        print(char, "Found")
        break
    print(char)
else:                                  #else is used to know whether we have reached the end of loop which checking the conditions.
    print("the end of for loop, character not found")
print("general end")


# range(): function that returns a sequence of numbers, starting from '0' by default and increments by '1' by default and stops before a specified number.

# range(stop condition)
seq = range(10) 
for i in seq:   #or for i in range(10)
    print(i)    # prints 0,1,2,3,4,5,6,7,8,9

# range(start[optional], stop)
for i in range(2,10):
    print(i)   # prints 2,3,4,5,6,7,8,9

# range(start[optional], stop, step[optional]) --> application: when printing all even numbers.
for i in range(2,10,2):  
    print(i)   # prints 2,4,6,8    

# pass statement: it does nothing. to avoid indentation error for & range function, it is used to skip or placeholder for the furture code.
# pass does nothing. Pass can also be used if else conditional statements also.
for i in range(5):
    pass
'''




# ---------------------------------------------------------------------Practice questions---------------------------------------------------------------------------------
'''
# 1.Print numbers from 1 to 100
count=1
while count <=100:
    print(count)
    count +=1

print("End of code") #optional

# 2.Print number from 100 to 1
count=100
while count >=1:
    print(count)
    count -=1
print("End of code")

# 3.Print the multipliocation table of a number 'n'
num=13
count=1
while count <=10:
    print("13 X ",count," = ", num*count)
    count +=1

print("This is the end of table")

# 4.Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100] using while loop
num_lst=[1,4,9,16,25,36,49,64,81,100]
index=0
while index <= (len(num_lst)-1):      #(len(num_lst)-1) is 10-1==>9(idex of the last element)
# (or) index < len(num_lst)
    print(num_lst[index])      # values of indices will be present one by one->num_lst[0], num_lst[1], .......num_lst[9]
    index+=1
print("End of code")

#(OR) using for loop as below,

num_lst=[1,4,9,16,25,36,49,64,81,100]

for num in num_lst:    #no need of index for iterating
    print(num)


# 5.Search for a number 'x' in the following tuple using while loop.

x=int(input("Enter the number (x): "))
num_tup=(1,4,9,16,25,36,49,56,81,100)

i=0
while i < len(num_tup):
    if(num_tup[i] == x):
        print("Found the element at index: ", i)
    i +=1

# (OR) 
# using for loop as below,
x=int(input("Enter the number (x): "))
num_tup=(1,4,9,16,25,36,49,56,81,100,49,49)
index=0  #added variable only to check what index position the value given was found.

for num in num_tup:
    if(num == x):
        print("The number matched and found at index: ", index)
    index +=1
    
# (OR) 
# using for loop with else as below,
x=int(input("Enter the number (x): "))
num_tup=(1,4,9,16,25,36,49,56,81,100)
index=0  #added variable only to check what index position the value given was found.

for num in num_tup:
    if(num == x):
        print("The number enetered is found", num)
        break
else:
    print("the number is not found")

# 6.Print numbers from 1 to 100 using for & range.
for i in range(1, 101):   #given start and stop conditions
    print(i)

# 7.Print numbers from 100 to 1 using for and range.
for i in range(100, 0, -1):   #stop condition 0: it stops before it that means: 1 which we want to print.
    print(i)

# 8.Print the multiplication table of a number 'n'

n=int(input("Enter number for its mutliplication table: "))
for i in range(1, 11, 1):
    print(n," x ", i, " = ", n*i)

# 9.Write a program to find the sum of first n natural numbers (using while loop) 1,2,3,4,5....

n=int(input("Enter the upto which natural number the sum is required: "))
i=1    #iterator
sum=0

while(i<=n):
   sum +=i
   i +=1
print("The sum of n natural numbers is: ", sum)

# (OR) using range():

n=100
sum=0

for i in range(1,n+1):
    sum +=i
print("The total sum: ", sum)
'''
# 10.Write a program to find the factorial of first n numbers. (using for & range)
# factorial means: The Factorial of a whole number 'n' is defined as the product of that number with every whole number less than or equal to 'n' till 1.
# n!= n*(n-1)*(n-2).....1














