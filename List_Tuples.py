# Lists and tuples in python

# List: built-in data type that stores set of values that can be of different types too.

student_list= ["Rama", 30, "Hyderabad"]
print(len(student_list), student_list) #list operations: length of list.

# Indexing in lists.
change_list=student_list[1] 
print(change_list)

#assigning. In lists, the indexing is mutational that means, the value accessed can be modified (unlike string indexing).
student_list[1]=24
print(student_list)

# Slicing: same rules as in string slicing.
print(student_list[1:10]) #sublist of the list.

# Negative indexing in lists: starts with -1 from left<--right. 

marks=[10,20,30,40,50] #50 is in the -1th position that shall not be included.
print(marks[-3:-1]) #shall print [30,40]


# List methods: these specific to list only.

# list.append()-> adds the value at the end.
marks=[20,60,30,40]
marks.append(50)
print(marks) #o/p: [20,60,30,40,50]

# list.sort()->sorts in ascending order, also can be done for alphabetic order.
print(marks.sort()) #sort doesnt return anything. It go and make changes in the original list.
print(marks) #you will see sorted list.

# list.sort(reverse=True)->sorts in descending order
print(marks.sort(reverse=True)) #sorts the list in descending in the original list
print(marks)

# list.reverse()->reverses the list.
print(marks.reverse()) 
print(marks)

# list.insert(idx,el)-> insert element at index.
lst1=["Rama", 30, "Btech"]
lst1.insert(1, 15)
print(lst1)

# now the list =['Rama', 15, 30, 'Btech']
# list.pop(ind)-> will help to remove particular element at index.
lst1.pop(2)
print(lst1) #removes the element at 2nd index i.e 30.

# list.remove()-> removes the first occurence of  the element.
lst2=['apple', 'banana', 'carrot', 'lichi', 'banana']
lst3=[2,1,3,1,4,1] 
lst3.remove(1) #deletes the first occurence of 1
lst2.remove('banana') #deletes the first occurence of 'banana' string.
print(lst2, lst3)


# Tuple: is a built-in data type that lets us create a immutable the sequence of values.
# Tuple object doesnt support item assignment just like strings.
# Tuple supports slicing just like strings adn list.

tup =(2,1,3,1,4,1,5)
print(tup[0], type(tup)) # element 2 is in the 0th position. also can print type of the data type. class 'tuple'

# Tuple slicing:
print(tup[1:3]) #prints (1,2) as they are the 1st and 2nd positions in the tuple.

# 2 important tuple functions.

# tup.index(el)-> returns the index of the first occurence of the element in the tuple.
tup =(2,1,3,1,4,1,5)
print(tup.index(2)) # element '2' is at the 0th position. 

# tup.count(el)-> returns no of the time a element occured in the tuple.
print(tup.count(1)) #element '1' has occured for 3 times in the tuple.


#--------------------------------------------------------------------Practice questions--------------------------------------------------------------------------------

# 1.ask the user to enter the names of the 3 favorite movies and store them in a list.

movie1=input("enter your 1st fav movie: ")
movie2=input("enter your 2nd fav movie: ")
movie3=input("enter your 3rd fav movie: ")

movie_list=[ movie1, movie2, movie3]
print("Your favorite movies are : ",movie_list)

#  (OR)

movies=[] # create a empty list and start appending the values inputted by the useer.
movies.append(input("enter the 1st movie:"))
movies.append(input("enter the 2nd movie:"))
movies.append(input("enter the 3rd movie:"))

print(movies)

# 2.Check if a list contains a palindrome of elements.

lst_original=['r','a','m','a']  # or the input can be lst_original=[1,2,3,2,1]
lst_copy=lst_original.copy()
lst_copy.reverse()
print(lst_copy) #The lst_copy is already reversed.

if(lst_original==lst_copy):
    print("Palindrome","\n","The original list is: ",lst_original,"\n","The Revered string is : ", lst_copy)
else:
    print("Not a Palindrome","\n","The original list is: ",lst_original,"\n","The Revered string is : ", lst_copy)

# 3.Write a program to count the number of students with 'A' grade in the tuple.
Student_grade=('C','D','A','A','B','B','A') # tuple
print(type(Student_grade),"\n","The number of students with Grade 'A' are: ",Student_grade.count('A'))

# 4.Store the above values in a list and sort them from 'A' to 'D'.
student_grades_list=['C','D','A','A','B','B','A'] #list
student_grades_list.sort()
print("The sorted student grades are: ",student_grades_list )



