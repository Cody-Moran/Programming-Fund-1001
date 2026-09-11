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

# printing a silly sentence
# %%
name = input("What is your name?: ")
adj = "hard"
verb = "jumped"
print(f"{name} {verb} really {adj}")
# %%
# price and quantity of item GST
# %%
item_price = float(input("What is the price of the item?: "))
quantity = float(input("Quantity: "))
gst = ((quantity*item_price)*0.05)
total = (item_price*quantity+gst)
print(f"Purchasing {quantity:.0f} of this item worth ${item_price} including the GST amount of $0.05 is ${total}")
# %%

