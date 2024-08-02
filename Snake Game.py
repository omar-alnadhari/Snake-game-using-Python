# Import modules necessary for the game
import random  #--> من اجل جعل الاكل يظهر بمكان عشوائي على الشاشة
import curses  #--> من اجل اضافة شكل الثعبان على الكونسول
# import os

# os.system('cls') #مسح المسارات التي تظهر في الكونسول

# Initialize the curses library to create our screen
screen = curses.initscr()  #--> screen الان تمثل الشاة كلها

# Hide the mouse cursor
curses.curs_set(0)  #-->   لها 3 قيم   0- مخفي     -1 باين     2- باين جدا   

# Getmax screen height and width
screen_height, screen_width = screen.getmaxyx() # عندما تعيد الدالة اكثر من قيمة لاكثر من متغير 
                                                # تسمى هذه الحركة في بايثون (unpacking)
# Create new wnidow
window = curses.newwin(screen_height, screen_width, 0, 0)

# Allow window to receive
window.keypad(1)  #-->

# Set the delay for updating the screen
window.timeout(100)  #-->

# Set the x , y coordinates of the initial position of snake's head
snk_x = screen_width // 4    # // --> called intger division
snk_y = screen_height // 2    # لجعل الثعبان يظهر منتصف الشاشة

# Define the initial position of the snake body
snake = [
    [snk_y, snk_x], #-> The head part
    [snk_y, snk_x - 1], #--> The middle of body
    [snk_y, snk_x - 2]  #--> The tail
]

# Create the food on middle of window
food = [screen_height // 2, screen_width // 2]

# Add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI) #-->

# Set initial movement direction to right
key = curses.KEY_RIGHT 

# Create game loops that loops forever untill player loses or quits
while True:
# Get the next key that will be pressed by user
    next_key = window.getch() #-->
    # If user doesn't input anything, key remians same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key
    # if next_key == -1:
    #     key = key
    # else:
    #     key = next_key

    # Check if snake collided with the walls or itself
    if snake[0][0] in [0,screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake[1:]:
    # If it collides close the window & exit programe
        curses.endwin() #--> Closing the window
        quit()  #--> Exit the program

    # Set new position of the snake based on the direction 
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -=1
    if key == curses.KEY_RIGHT:
        new_head[1] +=1
    if key == curses.KEY_LEFT:
        new_head[1] -=1
    
    # Insert the new head to the first position of snake list
    snake.insert(0,new_head)
    # Check  if snake ate the food
    if snake[0] == food:
        food = None # Remove food if snake ate it
    # while food its removed, generate new food in a random place on screen  with
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            # Set the food to new food if new food generated is not in snake body and add it to screen
            food = new_food if new_food not in snake else None
        window.addch(food[0],food[1],curses.ACS_PI)
    # Otherwise remove the last segment of snake body
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1],' ')

    
    # Update the position of the snake on the screen
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)