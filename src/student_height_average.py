#st_h = [180, 124, 165, 173, 189, 169, 146] # Student height.
st_h = input("Input a list of student heights [cm]: ").split() # Student height.
for n in range (0, len(st_h)):
    st_h[n] = int(st_h[n])
print(st_h)

sh = 0
for height in st_h:
    sh += height
print(sh)

nost = 0
for students in st_h:
    nost += 1
print(nost)

average = (round(sh / nost))
print (average)