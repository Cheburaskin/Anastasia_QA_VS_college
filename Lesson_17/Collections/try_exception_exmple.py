my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[0])  # This will raise an IndexError because index 10 is out of range
except IndexError:
    print("Index is out of range")
