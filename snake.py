import random
import curses

s = curses.initscr()
curses.curs_set(0)

height, width - s.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = width / 2
snake_y = height / 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

comida = [height/2,width/2]
window.addch(int(comida[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT