print("Welcome to the tip calculator")
total = float(input("what was the total bill? Rs"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
divide = int(input("How many people to split the bill? "))
tip_per = tip/100

amt = total*tip_per
total2 = amt+total
final = round(total2/divide, 2)
print(f"Each person should pay: Rs{final}")

