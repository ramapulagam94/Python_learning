#Strings and Conditional statements

# String: is a data type that stores a sequence of characters
# Escape sequence characters: used for formatting (for tab space, nextline (\n), etc.)

str1="Hello, I am Rama \n I am working in Cyient."
print(str1)

# String operations/functions: Look into google for more options

# 1. String concatenation
str1 = "Have "
str2 = "Good day"

print(str1 + str2)

# 2. String Length function len()
str1="Solar system"
print(len(str1))

# Indexing : when a string is created, internally a position is allocated each character. starting from the 0th position ... (left to right)
# A  p  n  a  C  o  l  l  e  g  e
# 0  1  2  3  4  5  6  7  8  9  10

str1="Apnacollege"
ch=str1[0] # A is in the 0th position of the string.
print(ch)
print(str1[1:4]) # is pna, 4th position value is not included.

# Slicing : Accessing parts of a string

str1 = "All-The-Best-Rama"
str2 = str1[0:4]         # is All-, 4th index value is ignored.
str3 = str1[1:len(str1)] # or str1[1:] is ll-The-best-Rama
print(str2, str3)

# Special case Slicing: Negative index, it starts from -1 (right to left) 
#  A  p  p  l  e
# -5 -4 -3 -2 -1

str = "Apple"
print(str[-3:-1]) # is pl
print(str[-5:-2]) # is App, the -2th position value is not included.

# String Functions: 
# str.endswith, str.capitalize, str.replace, srt.find, str.count etc.

#------------------------------------------------------------------Practice questions---------------------------------------------------------------------------------

# 1.Input user's first name and print its length

str1=input("Enter your first name: ")
print("Length of your name: ", len(str1)) #length is 4

# 2.Find the occurrences of '$' in string

name="I am Rama $, I am a coder $, I work for cyient."
print("the number of times '$' occured is: ", name.count("$"))


# Conditional statements:

# 1. if-elif-else statement:

marks=float(input("Enter the student marks: "))

if(marks>90):
    print("Grade: A")
elif(90>marks>=80):
    print("Grade: B")
elif(marks>=70 and marks<80):  #can also use logical operator.
    print("Grade: c")
else:
    print("The student marks are: ", marks, " and he needs to improve")

print("end of code")

# 2.Nesting:

age=int(input("Enter your age: "))

if(age>=18):
    if(age>80):
        print("Please don't drive")
    else:
        print("You can drive")
else:
    print("Underage, you shouldn't drive")

#----------------------------------------------------------------------------Practise questions--------------------------------------------------------------------------

# 1.Check if a number entered by user is odd or even.

num=int(input("Enter the number: "))

if(num%2==0):
    print("The number enter is even", num) # All even numbers are divisble by '2'
else:
    print("The number is odd", num)

# 2.Write a program to find the greatest of 3 numbers entered by user.

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

if(a==b==c):
    print("a,b,c have same value: ",a)
elif(a>=b and a>=c):
    print("a is greatest", a)
elif(b>=c):
    print("b is greatest", b)
else:
    print("c is greatest")

# 3.Write a program to find out the largest of 4 numbers.

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
d=int(input("enter d: "))

if(a==b==c==d):
    print("a,b,c,d have same value: ",a)
elif(a>=b and a>=c and a>=d):
    print("a is greatest", a)
elif(b>=c and b>=d):
    print("b is greatest", b)
elif(c>=d):
    print("c is greatest", c)
else:
    print("d is greatest", d)

# 4. Check if a entered number is a multiple of 7 or not.
# Note: any number divisble by 7 shall return reminder 0 when divided by 7.

num=int(input("Enter the number: "))

if(num%7==0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")

