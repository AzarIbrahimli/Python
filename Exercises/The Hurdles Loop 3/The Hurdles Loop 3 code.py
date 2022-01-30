def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_right()    
def check():
    while wall_in_front():
        turn_left()
        jump()        
def till_wall():
    while front_is_clear():
        while at_goal():
            done()
        move()

while at_goal!=True:
    till_wall()
    check()
    jump()
    till_wall()
    turn_left()
