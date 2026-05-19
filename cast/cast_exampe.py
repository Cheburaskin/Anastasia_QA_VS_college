a =5
b= "10"
b= int(b) # converts string to integer
print(a + b) # prints 15
c= 3.14
c= int(c) # converts float to integer, truncating the decimal part
print(c) # prints 3 
d= "3.14"
d= float(d) # converts string to float
print(d) # prints 3.14

greet = "Hello,_" + str(a) # converts integer to string and concatenates
print(greet) # prints Hello, _5