from typing import final
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_person = tip / 100
total_tip_amt = bill * tip_as_person
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person , 2)
print(f"each should pay ${final_amt}")
