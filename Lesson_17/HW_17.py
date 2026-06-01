#---- page 42 ---
str1 = input("Input string 1: ")
if str1.count('h') >= 2:
    print("OK")

#---- page 47 ---
collection1 = [5, 6, 4, 4, 5, 6, 4, 4, 5, 6, 4, 4]
print(collection1[0])
print(collection1[-1])
length = len(collection1)
collection1.append(length)
print(collection1)


#---- page 50 ---
num_collection = input("Please enter a collection of  4 numbers separated by spaces: ")
num_collection = num_collection.split()  # Split the input string into a list of strings
if len(num_collection) == 4:
    num_collection = [int(num) for num in num_collection]

    for num in num_collection:
        if num < 0:
            print(num)
else:
    print("Error: You must enter exactly 4 numbers.")


str_collection = input("Please enter a collection of  4 strings separated by spaces: ")
str_collection = str_collection.split()  # Split the input string into a list of strings
if len(str_collection) == 4:
    str_collection[0], str_collection[-1] = str_collection[-1], str_collection[0]
    print(str_collection)
else:
    print("Error: You must enter exactly 4 strings.")

grade_collection = [90, 85, 78, 92, 88]
count = 0
for grade in grade_collection:
    if grade >= 70:
        count = count + 1
print("Number of passing students: ", count)
        
#---- page 56 ---
def num_mult_by_2(num):
    print(num * 2)

num_mult_by_2(5)

def str_length_mult_by_2(text):
    return(len(text) * 2)

def str_last_char_is_exist_twice(text):
    if text.count(text[-1]) >= 2:
        return True
    else:
        return False
       
print(str_length_mult_by_2("My string length"))  
print(str_last_char_is_exist_twice("My string length")) 


