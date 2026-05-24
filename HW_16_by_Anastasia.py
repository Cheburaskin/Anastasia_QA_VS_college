#page 15

var_name1=10
var_name2=25
var_name3=3

var_average=round((var_name1+var_name2+var_name3)/3, 1)    
print("The age average is:", var_average)


#page22

input_string_1 = input("Please enter a string: ")
print("First character:", input_string_1[0])
print("Last character:", input_string_1[-1])
print("Middle character:", input_string_1[len(input_string_1) // 2])


while True: 
    input_string_2 = input("Please enter another string (at least 5 characters): ")
    if len(input_string_2) >= 5:
        string_3=input_string_2[2:]
        print("The string from the 3rd character is: ", string_3)
        print("The string lenght is: ", len(input_string_2))
        replaced_string = input_string_2.replace(" ", "-")
        print("Replaced string:", replaced_string)
        break
    else:   
        print("The string is too short. Please enter at least 5 characters.")


#page 26

input_int=int(input("Please enter an integer: "))
if input_int>=0:
    print("The integer is positive.")
else:
    print("The integer is negative.")

input_string_4 = input("Please enter a string: ")
if input_string_4[0]=="A":
    repped_string_4 = "a" + input_string_4[1:]
    print("Replaced string:", repped_string_4)

input_email = input("Please enter an email address: ")
if len(input_email) < 4:
    print("error: The email address is TOO SHORT")
elif input_email[0] == "@" or input_email[-1] == "@":
    print("error: The email is NOT VALID")


#page 29

input_int_2=int(input("Please enter another integer: "))
if input_int_2==-1:
    print("a")
else:
    print("b")

#page 30

input_int=int(input("Please enter an integer: "))
if input_int>=0:
    print("The integer is positive.")
elif input_int<0:
    print("The integer is negative.")
if input_int%2==0:
    print("The integer is even.")
else:
    print("The integer is odd.")


#page 32
input_string_5 = input("Please enter a string: ")
length_string_5 = len(input_string_5)
if length_string_5 < 4:
    print("The string is too short.")
elif length_string_5 > 9:   
    print("The string is too long.")
else:
    print("The string is OK.")

   
#page 34

age = int(input("Please enter your age: "))
if age < 0:
    age=0
    print("Age cannot be negative. Setting age to 0.")
elif age > 120:
    age=120
    print("Age cannot be greater than 120. Setting age to 120.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
 
while True: 
    password = input("Please enter a password: ")
    if len(password) > 8:
        if password[-1]=="$":
            if password[0] == "Z" or password[0] == "C":
                print("STRONG PASSWORD.")
                break
            else:
                print("The password does not start with 'Z' or 'C'.")
        else:
            print("The password does not end with $.")
    else:
        print("The password is less than 8 characters.")

#page 41
num=-5
while num <= 8:
    print("num is:", num)
    num += 1

num1=2
while num1 <=16:
    print(num1)
    num1 += 2

    

input_mail = input("Please enter your email address: ")
at_sign_count= input_mail.count("@")
print("The number of @ signs in the email is:", at_sign_count)
