import random

print("Welcome to the PyPass Generator!")
letters = int(input("\nHow many letters would you like in your password: "))
symbols = int(input("\nHow many symbols would you like?: "))
numbers = int(input("\nHow many numbers would you like?: "))

l_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
n_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = ""
password_list = []

for char in range(1, letters + 1):
    l_char = random.choice(l_list)
    password_list.append(random.choice(l_list))
    password += l_char

for symb in range(1, symbols + 1):
    s_char = random.choice(s_list)
    password_list.append(random.choice(s_list))
    password += s_char

for num in range(1, numbers + 1):
    n_char = random.choice(n_list)
    password_list.append(random.choice(n_list))
    password += n_char

print("Your basic password is: ",password)

# Add adv form soon.