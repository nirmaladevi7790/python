#nested if else statement prg
print("welcome to the roller coaster")
height=int(input("what is your height in cm?"))
if height>=120:
    print("you are eligible for roller coaster ride!")
    age=int(input("what is your age?"))
    if age>=12:
        print("you have to pay $5:")
    elif age<=18:
        print("you have to pay $10:")
    else:
        print("you have to pay $20")
else:
    print("sorry! you have to grow taller before you can ride") 
