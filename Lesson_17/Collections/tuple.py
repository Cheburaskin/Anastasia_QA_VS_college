WEEK_DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

for day in WEEK_DAYS:
    print(day)


my_Set = {"A", "A", "I", "J"}

for item in my_Set:
    print(item)
print("length of the set is:", len(my_Set))
print(my_Set)

Alice = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}

print(Alice["name"])  # Output: Alice
print(Alice["age"])   # Output: 30 

Moshe = {
    "name": "Moshe",
    "age": 25,
    "city": "Tel Aviv",
    "email": "moshe@example.com"
}

student_list = [Alice, Moshe]

for student in student_list:
    print(student["name"], student["age"], student["city"], student["email"])
    