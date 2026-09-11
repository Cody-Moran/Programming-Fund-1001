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

# kilometers to miles converison
# %%
km = float(input ("Enter number of kilometers: "))
miles = km*0.621371
print(f"{km} converted into miles is: {miles:.2f}")
# %%
 
# fuel consumption calculation (cost of trip)
# %%
dist = float(input ("Enter the distance you want to travel (km): "))
vehicle_consum = float(input ("Enter the fuel consumption of your vehicle (liters per 100km): "))
price_per_litre = 1.58
fuel_consum = (vehicle_consum*price_per_litre)
trip_consum = (dist)*(fuel_consum)/100
print(f"You are traveling {dist} kilometers, the amount of fuel needed for that distance is {vehicle_consum:.1f} liters. With the price of fuel being ${price_per_litre} per litre, this trip will cost ${trip_consum:.2f}")
# %%
