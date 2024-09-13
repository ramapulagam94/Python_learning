# Dictionaries and Set

# Dictionary is the built-in datatype(dict_type) that is used to store the data values in the form of Key:Value pairs. It can comprise of different datatypes. The key is mostly a string.
# Just like our hand dictionary
# Dictionaries are unordered(as no indexing), mutable. Doesn't allow duplicate keys.

info={
    "Name": "Rama", 
    "Organization": ["Cyient", "TechMahindra"], 
    "Skills": ("Python", "Testing"), 
    "Age" :30, 
    "Is Adult": "True",
}

info["Name"]="Sri Ramya" #for changing the value of a key. Accessed through key and changed. (Name is key here).
info["Surname"]="Pulla"  #for adding new key:value pair into the dictionary info. Surname will be added at the last.

print(info)

# Nested Disctionary:

student={
    "Name" : "Rama",
    "Subject" : {              #Subject is a key which has again a dictionary inside it. 
        "Phy"  : "90",         #Phy, chem, math are the keys.
        "Chem" : "80",
        "Math" : "70"
    }
}
print(student["Subject"]["Math"]) #will print 70

# Dictionary Methods:

# 1.mydict.keys()-->return all keys.
print(student.keys())   # print: dict_keys(['Name', 'Subject'])

print(list(student.keys())) #-->Typecasting from (dict_type to list datatype). o/p: ['Name', 'Subject']
print(len(list(student.keys()))) #finding the length of list.

# 2.mydict.values()-->return all values.
print(student.values())  # prints: dict_values(['Rama', {'Phy': '90', 'Chem': '80', 'Math': '70'}])

# 3.mydict.items() -->return all key, value pairs in the form of tuples. The output in () paranthesis.
print(student.items())  #prints: dict_items([('Name', 'Rama'), ('Subject', {'Phy': '90', 'Chem': '80', 'Math': '70'})])

# 4.mydict.get("key") -->returns the key according to value.
print(student.get("Name")) # (or) we can use print(student["Name"]) also.

# what is the difference between these two statement:
#     student.get("key which is non-existent")--> will return 'none'
# but student["key which is non-existent"] --> will get error, to avoid faliures beyond this step.

# mydict.update(new Dict)--> inserts the specified items to the existing dictionary.
student.update({"City" : "Hyderabad"})
print(student)    #output: {'Name': 'Rama', 'Subject': {'Phy': '90', 'Chem': '80', 'Math': '70'}, 'City': 'Hyderabad'}

# Set: Is also a collection of unordered items. each element in the se tis immutable. 
# Math set theory based. Duplicate values are ignored while printing or performing any operations.

collection={1,2,"Rama", "Cyient", "Rama"}
print("Length of the set is: ", len(collection),"and ", "The elements are:", collection)
# Output:
# Length of the set is:  4 and  The elements are: {1, 2, 'Cyient', 'Rama'}

# Empty set: 
 
nums = set() 
print(type(nums), nums) 

# Set methods:

# 1. set.add(el)--> adds an element of any datatype except list and dictionary.
collection1=set()
collection1.add(1) #int
collection1.add("Rama") #string
collection1.add((10,20,"Rama", "Viny")) #tuple

print(collection1)    #o/p:{1, 'Rama', (10, 20, 'Rama', 'Viny')}

#unhashable value.
collection1.add([99,999,9999]) 
print(collection1)    #will output: TypeError: unhashable type: 'list'

# 2. Set.remove(el)--> removes an element
collection1=set()
collection1.add(1)
collection1.add("Rama")
collection1.add((10,20,"Rama", "Viny"))
collection1.remove(1)
print(collection1)   #o/p: 1 is removed and {(10, 20, 'Rama', 'Viny'), 'Rama'}

# set.clear()--> empties the set
collection2=collection1.copy()
print(collection2)
collection2.clear()
print(collection2) #o/p: set()

# set.pop()-->removes a randow element.
print(collection1.pop())  #poped up tuple and printed string-{'Rama'}. the deletion is random.

# Set.union(set2) -> Combines both the sets and returns a new set with unique values.
# set.intersection(set2) -> combines common values and returns the new set.

set1={1,2,3}
set2={3,4,5} # 3 is common in both the sets.

print(set1.union(set2)) # will return {1,2,3,4,5}
print(set1.intersection(set2)) # will return {3}
print(set1)
print(set2) #set1,set2 values unchanged.

#--------------------------------------------------------------Practice questions--------------------------------------------------------------------------------

# 1.Store the following word meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

dict_book={
    "table": ("a piece of furniture", "list of facts & figures"), #written as tuple as it has 1 key and multiple values, then we have to use list[] or tuple()
    "cat" : "a small animal"
}
print(dict_book)


# 2. Find out how many classrooms required for each subject of the students. Assume 1 classroom per subject.
# "python", "java", "C++", "python", "javascript", java", "python", "java", "C++", "C"

set_subjects={"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(set_subjects), set_subjects) 
# len(set name)--> will return no. of unique subjects and set_subjects-> will return all unique values of the sets.

# 3. Write a program to enter marks of 3 subjects from the user and them in a dictionary.Start with an empty set and add 1 by 1.
#    Use subj as 'key' and marks as 'value'.

Subj_dict={} #create an empty dictionary

x=int(input("Enter physics marks: "))
Subj_dict.update({"Phy": x})

y=int(input("Enter chemistry marks: "))
Subj_dict.update({"Chem": y})

z=int(input("Enter math marks: "))
Subj_dict.update({"Math": z})

print(Subj_dict)  # output: {'Phy': 97, 'Chem': 98, 'Math': 96}

# 4. Frigure out a way to store 9 and 9.0 as seperate values in set.

# 1st solution: store 9.0 as string in set.

value_set={9, "9.0"}
print(value_set)

# (or) 2nd solution: use of built-in data type tuple.

values={("Float", 9.0), ("Int", 9)}
#           tuple1         tuple2
print(values)

