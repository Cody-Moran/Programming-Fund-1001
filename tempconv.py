# temp conversion program
# the formula is °F = (°C × 9/5) + 32

user_input = float(input("Input celsius temp here: "))
output = user_input*9/5+32
print(f"{user_input} celsius converted to farenheit is: {output}")

# height and width of rectangle calculation

width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))
area = width * height
perimeter = 2*(area)

print(f"Area: {area:.3f}")  