
def calculte_price_with_tax(price: float, tax: float=17.0):
    """
    Calculates the price including tax.
    Args:
        price (float): The base price.
        tax (float, optional): The tax percentage. Defaults to 17.0.
    Args:
        price (float): The original price.
        tax (float, optional): The tax percentage to apply. Defaults to 17.0.

    Returns:
        float: The price including tax.
    """
    result = price + (price * tax / 100)
    return result

print(calculte_price_with_tax(100))  # Output: 117.0    


#---page 56----

def is_end_character_exist_in_text(text: str) -> bool:  
    """
    Checks if the specified end character exists in the given text more than once.
    Args:
        text (str): The text to check.
    Returns:    
        bool: True if the end character exists, False otherwise.
    """
  #  last_char=text[-1]
   # if last_char in text [0:-2]:
   #     return True
    #return False
    return text.count(text[-1]) > 1

text = "?Hello, how are you doing today?"
print(is_end_character_exist_in_text(text))  # Output: True