def count_char_in_string(text="texxt text", char="a"):
    count=text.count(char)
    return count

input_string_5 = input("Please enter a string: ")
input_char = input("Please enter a character to count: ")
count=count_char_in_string(input_string_5, input_char)
print(count)   