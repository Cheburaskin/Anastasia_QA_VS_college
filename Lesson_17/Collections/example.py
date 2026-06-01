my_list = ["tiger", "lion", "elephant", "giraffe", "zebra"]

print(my_list[0])  # Output: tiger
print(my_list[2])  # Output: elephant
print(my_list[4])  # Output: zebra
print(my_list)

for item in my_list:
    if item.startswith("z") or item.startswith("t"):
        print(item)

my_list.append("monkey")
print(my_list)
my_list.insert(2, "bear")
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)