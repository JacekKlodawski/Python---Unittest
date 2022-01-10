width = int(input("Enter the width of the rectangle"))
assert width > 0, "The width value must be positive"
length = int(input("Enter the length of the rectangle"))
assert length > 0, "The length value must be positive"

area = width * length
print(f'Area: {area}')
