import random

word_list = ["ardvark", "camel", "hamster", "babboon"]

hang_word = random.choice(word_list)

hang_word_len = (len(hang_word))
hang_list = []
for letter in range(hang_word_len):
    hang_list.append("_")

print("\nThe word is:",hang_word,"\n")
print(hang_list)
guess = input("Guess a letter: ").lower()

for letter in hang_word:
    if letter == guess:
        print(f"Correct:", guess)
    else:
        print("Wrong")