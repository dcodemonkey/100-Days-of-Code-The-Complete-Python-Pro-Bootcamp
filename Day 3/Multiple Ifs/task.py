print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youths tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    want_photo = input("Do you want photos of your ride? Type y for Yes and n for No. \n")
    if want_photo == 'y':
        bill += 3
    print(f"You're final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
