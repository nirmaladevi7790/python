#multiple if statement in succession
print("welcome to the rollercoaster!")
height=int(input("waht is your height in cm?"))
bill=0
if height>=120:
    print("you can ride the rollercoaster")
    age=int(input("what is your age?"))
    if age<=12:
        bill=5
        print("child tickets are $5.")
    elif age<=18:
        bill=7
        print("child tickets are $7.")
    else:
        bill=12
        print("adult tickets are $12.")
wants_photo=input("Do you want a photo taken? y or N")
if wants_photo=="y":
    bill+=3
    print(f"your final bill is $ {bill}") 
else:
    print("sorry,you have to grow taller before you can ride.")
