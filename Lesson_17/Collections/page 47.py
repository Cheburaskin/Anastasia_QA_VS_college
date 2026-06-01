my_list=[1,3,45,7,8,9,23,6,98,54,34,56,78,90,13,45,89]
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 0
list_length = len(my_list)  # Output: 18
my_list.append(list_length)  # Adds "18" to the end of the list
print(my_list)  # Output: [1, 3, 45, 7, 8, 9, 23, 6, 98, 98754, 34, 56, 78, 90, 123, 456, 789, 0, "18"]
print("length of the list is:", list_length)  # Output: length of the list is: 18
count_pass_students = 0
for item in my_list:
    if item > 70:
        count_pass_students += 1
        print(item)
print(f"Number of passing students: {count_pass_students}//{len(my_list)}")  

find_name = "Bob"
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
exist = False
for student in students:
    if student == find_name:
        exist = True
        break
print("The name ", find_name, "is exist:", exist)
