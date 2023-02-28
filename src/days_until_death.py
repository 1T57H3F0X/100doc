age = input("What is your age?  [yr]: ")

age_as_int = int(age)

yr_remaining = 90 - age_as_int
days_remaining = yr_remaining * 365
weeks_remaining = yr_remaining * 52
month_remaining = yr_remaining * 12

print(f"\nYou have this long left: {yr_remaining} years, {month_remaining} months, {weeks_remaining} weeks, and {days_remaining} days.")