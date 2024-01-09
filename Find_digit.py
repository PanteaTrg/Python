import re


def find_largest_number(input_string):
    # Extract all numbers from the input string using regular expression
    numbers = [int(match) for match in re.findall(r'\d+', input_string)]

    if numbers:
        # Find the maximum number
        max_number = max(numbers)
        return max_number
    else:
        return None  # No numbers found in the input string


# Example usage:
input_string_two = '13twenty209sixty123'
result = find_largest_number(input_string_two)

if result is not None:
    print(f"The largest number in the input string is: {result}")
else:
    print("No numbers found in the input string.")
