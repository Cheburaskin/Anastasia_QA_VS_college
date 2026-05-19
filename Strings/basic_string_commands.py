str1= "Hello World"

print(str1[0]) # prints H
print(str1[1]) # prints e
print(str1[2]) # prints l
print(str1[3]) # prints l
print(str1[4]) # prints o

print(str1[-1]) # prints d
print(str1[-2]) # prints l


s_name= "John Doe"
print(s_name[0:4]) # prints John
print(s_name[5:8]) # prints Doe
print(len(s_name)) # prints 8
replace_name= s_name.replace("John", "Jane")
print(replace_name) # prints Jane Doe

print(s_name.upper()) # prints JOHN DOE
print(s_name.lower()) # prints john doe 
print(s_name.split()) # prints ['John', 'Doe']
print("join" in s_name.lower()) # prints True