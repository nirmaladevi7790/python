#CREATE A PRM USING F-STRINGS HOW MANY DAYS,WEEKS,MONTHS LEFT UNTIL 90 YEARS OLD
age = input("What is your current age? ")
total=90-int(age)
days=total*365
weeks=total*52
months=total*12
print(f"you have {days}days,you have {weeks}weeks,you have{months}months left")
