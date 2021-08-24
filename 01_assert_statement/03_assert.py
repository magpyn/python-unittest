width = int(input("Enter the width of the rectangle:"))
assert width > 0, "The width value must be positive"
height = int(input("Enter the hight of the recantagle:"))
assert height > 0, "The hight value must be positive"

area = width * height
print(f"Area is: {area}")