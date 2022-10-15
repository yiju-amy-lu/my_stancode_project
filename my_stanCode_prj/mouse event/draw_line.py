"""
File: draw_line
Name: Yi-Ju Lu
-------------------------
When number of clicking mouse is odd, window would create a ball.
When number of clicking mouse is even, window would add a line and remove the ball.
Lines would be remained.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# Constant
SIZE = 10
# Global variables
window = GWindow(width=800, height=400)
count = 1
ball_x = 0
ball_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # listen mouse
    onmouseclicked(appear)


def appear(mouse):

    global count, ball_x, ball_y

    # Check
    if count % 2 != 0:
        # define ball
        ball = GOval(SIZE, SIZE)
        ball.filled = False
        window.add(ball, mouse.x-SIZE/2, mouse.y-SIZE/2)
        ball_x = mouse.x
        ball_y = mouse.y
    else:
        ball = window.get_object_at(ball_x, ball_y)
        window.remove(ball)
        # define line
        line = GLine(ball_x + SIZE / 2, ball_y + SIZE / 2, mouse.x, mouse.y)
        window.add(line)

    # when clicking, count + 1 for defining check condition
    count += 1


if __name__ == "__main__":
    main()
