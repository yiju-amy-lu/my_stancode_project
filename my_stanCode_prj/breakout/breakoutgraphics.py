"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE:
Breakout project: coder site
Name: Yi-Ju Lu
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
# constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # set switch
        self.switch = False
        self.scores = 0

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # set label
        self.label = GLabel('Your scores: '+str(self.scores))
        self.label.color = 'blue'
        self.label.font = '-20'
        self.window.add(self.label, 0, self.label.height+2)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, window_width / 2 - ball_radius, window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.paddle_tracker)
        onmouseclicked(self.go)
        # Draw bricks
        for i in range(0, BRICK_ROWS):
            for j in range(0, BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                # define brick color
                if j/2 < 1:
                    brick_color = 'red'
                elif j/2 < 2:
                    brick_color = 'orange'
                elif j/2 < 3:
                    brick_color = 'yellow'
                elif j/2 < 4:
                    brick_color = 'green'
                else:
                    brick_color = 'blue'
                self.brick.fill_color = brick_color
                self.brick.color = brick_color
                brick_x = (BRICK_WIDTH+BRICK_SPACING)*i
                brick_y = BRICK_OFFSET+(BRICK_HEIGHT+BRICK_SPACING)*j
                self.window.add(self.brick, brick_x, brick_y)

    def paddle_tracker(self, event):
        """
        when mouse moved, the paddle will also move
        the center of the paddle will be same as the mouse
        but the height of the paddle will not change
        """
        if event.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        else:
            self.paddle.x = event.x - PADDLE_WIDTH / 2

    def go(self, event):
        """
        when mouse moved, the paddle will also move
        the center of the paddle will be same as the mouse
        but the height of the paddle will not change
        """
        self.switch = True
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy
