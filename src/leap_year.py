year = int(input("What year is it?  [yr]: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("\nYou are in a leap year!\n")
        else:
            print("\nIt is not a leap year.")
    else:
        print("\nIts a leap year!")
else:
    print("\nIt is not a leap year.")