def turn_right():
    turn_left()
    turn_left()
    turn_left()

i = 1
while i < 7:
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    if i == 7:
        break
    i += 1
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
