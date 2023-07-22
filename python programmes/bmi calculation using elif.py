#bmi calcualtion using if condition statement
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=round(weight/height**2)
if bmi < 18.5:
    print(f"you are bmi {bmi},you are underweight")
elif bmi<25:
    print(f"your bmi {bmi},you are normal weight")
elif bmi<30:
    print(f"your bmi {bmi},you are slightly overweight")
elif bmi<35:
    print(f"your bmi {bmi},you are obese")
else:
    print(f"your bmi {bmi},you are cilinically obese")
