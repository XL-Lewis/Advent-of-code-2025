import re


def is_repeating_substring(number_string):
    # Regular expression to match repeating substrings
    pattern = r"^(\d+)\1+$"

    # Check if the pattern matches the input string
    return bool(re.match(pattern, number_string))


with open("Day2/input.txt", "r") as file:
    first_line = file.readline().strip()
counter = 0

product_ranges = first_line.split(",")
for product_range in product_ranges:
    range_counter = 0
    product_range = product_range.split("-")

    l = int(product_range[0])
    r = int(product_range[1])

    for product_int in range(l, r + 1):
        product = str(product_int)
        if is_repeating_substring(product):
            range_counter += product_int
    print(f"Range {product_range} - counter: {range_counter}")
    counter += range_counter
print(counter)
