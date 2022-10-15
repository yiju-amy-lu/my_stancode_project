"""
File: bouncing ball
Name: Yi-Ju Lu
-------------------------
This program is designed to play the bouncing ball game.
When user clicked the mouse, ball would drop down
at a constant horizontal speed(VX) and a non-constant vertical speed(vy).
When ball hit the floor, ball would reflect with a 10% reducing energy.
The game would stop after ball hit the wall of right side 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0
switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch, count
    # Set ball at original place
    set_ball()
    # when mouse is clicked, program started
    onmouseclicked(drop)
    while True:
        if switch:
            count += 1
            vy = 0
            # Check if ball hit wall larger than three times, if yes, stop program
            while count <= 3:
                # Update
                ball.move(VX, vy)
                # Check
                if vy >= 0:
                    vy += GRAVITY
                if vy < 0:
                    vy += GRAVITY
                if ball.y + ball.height >= window.height:
                    vy = - (vy * REDUCE)
                if ball.x + ball.width >= window.width:
                    set_ball()
                    switch = False
                    break
                # Pause
                pause(DELAY)
        pause(DELAY)


def drop(mouse):
    global switch
    if count < 3:
        switch = True


def set_ball():
    ball.filled = True
    ball.fill_color = "red"
    ball.color = "red"
    window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
