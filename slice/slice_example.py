text="adfsdgfgnfgnghb"
print(text[0:5]) # prints characters from index 0 to 4
print(text[5:10]) # prints characters from index 5 to 9
print(text[10:15]) # prints characters from index 10 to 14
print(text[15:20]) # prints characters from index 15 to 19
print(text[0:20:2]) # prints every second character from index 0 to 20
print(text[::3]) # prints every third character from the entire string
print(text[::-1]) # prints the string in reverse order
print(text[-5:]) # prints the last 5 characters of the string
print(text[:5]) # prints the first 5 characters of the string

text2 = "123 5"
print(text2[0]) # prints 1
print(text2[-1]) # prints 5
print(text2[len(text2)//2]) # prints 3
print(text2[2:4]) # prints 34
print("String length: ", len(text2)) # prints the length of the string
print("Replace space with dash: ", text2.replace(" ", "-")) # prints 123-5
print(f"Is '5' in text2? {'5' in text2}") # prints True
