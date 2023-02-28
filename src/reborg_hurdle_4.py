def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def climber():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def wall_clear():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if at_goal():
        break
    if wall_in_front():
        climber()
    if front_is_clear():
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
