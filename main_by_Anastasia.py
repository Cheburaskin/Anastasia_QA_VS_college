print("Hello, World!")

#Section 1: Variables

username  = "Anastasia Kipns"
age       = 42
is_connected = True
score     = 100.0
tests_qnt = 5
test_passed = True

print("\n---Original Data---")
print("User:", username)
print("Age:", age)
print("Connected:", is_connected)
print("Score:", score)

#Section 2: Change Values

age = 43
score = 99.5
is_connected = False


print("\n---Updated Data---")
print("User:", username)
print("Age:", age)
print("Connected:", is_connected)
print("Score:", score)

#Section 3: Inputs

username = input("\nEnter your name?\n")
age = int(input("Enter your age?\n"))

print("Hello, ", username, "!")

#Section 4: Challange

username = input("\nEnter your name?\n")
tests_qnt = int(input("Enter an amount of tests you run: "))
if tests_qnt < 0:
    print("Invalid number of tests. Please enter a non-negative integer.")   
else:
    print("Tester", username, " ran ", tests_qnt, " tests today.")

# Section 5 - Boolean + if

test_passed = input("Did the test pass? (True/False)").strip().lower() == "true"

if test_passed:
    print("Test passed")  
else:   
    print("Test failed")