"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
Breakout project: user site
Name: Yi-Ju Lu
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# constants
FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    """
    While the user clicked the mouse, ball will start move
    1. if the ball hit walls or the paddle, ball will reflect
    2. if the ball hit bricks:
        ball will reflect, the brick which is hit will be removed, and the score will increase
    3. if the live = number of attempts, game over
    """
    graphics = BreakoutGraphics()
    window = graphics.window
    ball = graphics.ball
    label = graphics.label
    score = graphics.scores
    lives = 0  # define initial live

    # Add the animation loop here!
    while True:
        # while the user clicked the mouse, the switch would turn on, and lives increase
        if graphics.switch:
            vx = graphics.get_vx()  # get the velocity from coder site, b/c velocity can't be seen
            vy = graphics.get_vy()
            lives += 1
            while lives <= NUM_LIVES:
                # Update
                graphics.ball.move(vx, vy)
                # Check wall
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = -vx
                # check top of the wall, no need to check bottom of the wall
                if graphics.ball.y <= 0:
                    vy = -vy
                # check peddle or brick
                obj = obj_check(window, ball)
                if obj is graphics.paddle:
                    # when hit the paddle, not causing the ball stick on the paddle
                    if graphics.paddle.y <= ball.y + ball.height <= graphics.paddle.y+graphics.paddle.height/2:
                        vy = -vy
                # since brick only means the last brick, obj can not use graphics.bricks
                if obj is not None and obj is not graphics.paddle and obj is not graphics.label:
                    vy = -vy
                    graphics.window.remove(obj)
                    score += 1
                    label.text = 'Your scores: '+str(score)
                # check under paddle
                if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    if lives <= NUM_LIVES:
                        graphics.window.remove(graphics.ball)
                        graphics.window.add(graphics.ball, (window.width-ball.width)/2, (window.height-ball.height)/2)
                        graphics.switch = False
                    if lives == NUM_LIVES:
                        graphics.window.remove(graphics.ball)
                        graphics.window.add(graphics.ball, (window.width-ball.width)/2, (window.height-ball.height)/2)
                        graphics.switch = False
                        label.text = 'You lose! :('
                    break
                # winning condition
                if score == 100:
                    label.text = 'Congratulations, You win! Your scores: '+str(score)
                    graphics.window.remove(graphics.ball)
                    break
                # Pause
                pause(FRAME_RATE)

        # Pause
        pause(FRAME_RATE)


def obj_check(window, ball):
    obj1 = window.get_object_at(ball.x, ball.y)  # check left top
    obj2 = window.get_object_at(ball.x + ball.width, ball.y)  # check right top
    obj3 = window.get_object_at(ball.x, ball.y + ball.height)  # check left bottom
    obj4 = window.get_object_at(ball.x + ball.width, ball.y + ball.height)  # check right bottom
    if obj1 is not None:
        return obj1
    elif obj2 is not None:
        return obj2
    elif obj3 is not None:
        return obj3
    elif obj4 is not None:
        return obj4
    else:
        return None


if __name__ == '__main__':
    main()
