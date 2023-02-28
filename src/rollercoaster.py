height = int(input("How tall are you? [cm]: "))

if height >= 120:
    age = int(input("\nYou can ride the rollercoast, \nbut what is your age? [yr]: "))
    if age <= 12:
        price = 5
        print(f"\n{age} year olds must pay £5.\n")
    elif age <= 18:
        price = 7.50
        print(f"\n{age} year olds must pay £7.50.\n")
    elif age >= 45 and age <= 55:
        price = 0
        print(f"\n{age} year olds don't have to pay, it's free!")
    else:
        price = 10
        print(f"\n{age} year olds must pay £10.\n")

    photo_req = input("Do you want a photo for an extra £3? [y/n]: ")
    if photo_req == "y":
        photo_cost = 3
        bill = price + photo_cost
        print(f"\nYour total is £{bill}, enjoy the ride!\n")
    if photo_req == "n":
        bill = price
        print(f"\nYour final is £{bill}, enjoy the ride!\n")


else:
    print(f"\nYou must be over 120cm, your height is {height}cm which isn't tall enough. Sorry!")