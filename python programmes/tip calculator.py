#tip calculator
print("welcome to the tip calculator")
bill=float(input("what was the total bill?$"))
tip=int(input("how much tip would you like to give?10,12, or 15?"))
people=int(input("how many people to split the bill?"))
total_tip=bill*tip/100
total_amnt=total_tip+bill
total_peoplesplit=total_amnt/people
final_amount=round(total_peoplesplit,2)
final_amount="{:.2f}".format(total_peoplesplit)
print(f"each person should pay:${total_peoplesplit}")
