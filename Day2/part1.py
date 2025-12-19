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
        product = list(str(product_int))
        if len(product) % 2 == 1:
            pass
        else:
            if product[0 : int(len(product) / 2)] == product[int(len(product) / 2) :]:
                range_counter += product_int
    print(f"Range {product_range} - counter: {range_counter}")
    counter += range_counter
print(counter)
