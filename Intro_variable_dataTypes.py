# To comment out multplie lines of codes 3 ways:
# 1. select the lines and press cntrl + / for commenting out and un-commenting out.
# 2. """ """
# 3. ''' '''

# Single-line stmts.
print('Hello, my name is Rama and I am', 23, "I wish to become Azure data engineer")

# Multi-line stmts.
print('''
       Hello, my name is Rama and 
       I am 23, 
       I wish to become Azure data engineer
      ''')

# variables

# 1-print the value of varaibles.
name = "Rama" #String
age = 23 #integer
price = 30.123 #float

print("My name is ", name)
print("My age is ", age)

# 2-Print type of the variables

print(type(name))
print(type(age))


# Print sum/diff of 2 numbers
a=20
b=10
sum=a+b
diff=a-b
print(sum, diff)
print(" The sum of two numbers is", sum, "and the difference of two numbers is", diff)


# Operators

# 1. Arithemetic operators
a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #gives the reminder
print(a**b) #power

# 2. Relational or comparision operators: ==,!=,<,>,<=,>=. They are used in conditional statements
a=10
b=20

print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)

# 3. Assignment operations: =, +=, -=, *=, /=, %=, **=
num=10
#num= num + 10 (or) num +=10 , output is same.
num +=10

print("num :", num)

# 4. Logical operators: not, and, or
a=2
b=3

# not operators works on single operand.
print(not (a>b)) # 2>3 is flase but as we put not, it shall return True.
print( not True) #will return False

# and, or operator works on 2 operands
#1 program
val1= True
val2= False
print("AND operator is:", val1 and val2) #will return False as one of the val1,val2 is False and for TRUE both of them shall be TRUE.
print("OR operator is :", val1 or val2) #shall return True as one of the val1,val2 is True

#2 program
a=2
b=3
print("OR operator", a==b or a<b) # a==b is False, a<b is TRUE, the outcome shall be True as one of thm is True.

# Type Conversion: 
# 2 types: Conversion(python automatically converts)-->implicit
#          Casting (forceably convert one type to other)--> Explicit

# 1-implicit conversion
a=2
b=2.5
sum=a+b
print(type(sum), "and the sum is :", sum)

# 2-Type casting-->explicit conversion float
a = 2 #string type
b = 2.5
c= int("20") #convert string "20"-> int 20

sum = a+b+c
print(type(sum), "sum is:", sum) #sum will be float type.

# 3-Type casting-->explicit conversion string
a="100.2"
a =str(a)

print(type(a))

# Input statement in the Python

# input()-> result of input function is always a string (str) type.
# int(input())-> int
# float(input())->float

# 1
name= input("enter your name:") #enter name during execution
print("Welcome", name) # press 'enter' after entering your name in terminal.

# 2
age=int(input("enter you age: "))
print(type(age), "Hi, your age is: ", age)

#------------------------------------------------------------------------ Practise questions--------------------------------------------------------------------------

# 1.Input 2 numbers and print their sum

a = int(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

sum=a+b
print(type(sum), "The sum of 2 numbers is : ", sum) 
# (OR)
print("the sum is ", a+b)

# 2.Input a side of a square and print its area.
 
a=int(input("enter the side of a suqare (a): "))
print("The area of a square is (a x a): ", a * a) # or print("area:", a ** 2)

a=5
a **=2
print(a) #output is '25'

# 3. Input 2 floating numbers and print their average

a=float(input("Enter 1st number: "))
b =float(input("Enter 2nd number:"))

avg=(a+b)/2
print("The average of 2 number: ", avg)

# 4.Input 2 numbers, Print 'True' if a>= b. If not False

a=int(input("enter a: "))
b=int(input("enter b: "))

print("result of the condition= ", a>=b)