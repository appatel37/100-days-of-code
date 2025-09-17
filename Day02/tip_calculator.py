print("Welcome to the tip calculatior!")

bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_percent = tip / 100
total = bill * tip_percent
total_bill = bill + total
per_person_bill = total_bill/people
each_person = round(per_person_bill, 2)

print(f"Each person should pay: ${each_person}")