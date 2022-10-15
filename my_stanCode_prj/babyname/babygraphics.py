"""
File: babygraphics.py
Name: Yi-Ju Lu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
# Constant
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = int((width / len(YEARS)) * year_index) + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # create each line for each year
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i), GRAPH_MARGIN_SIZE - 10,
                           get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + 10,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # make factor used in the calculation of x,y position
    x_factor = int((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    y_factor = int(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
    y_over1000 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    # nested for-loop to check name & year
    for i in range(len(lookup_names)):
        lookup_name = lookup_names[i]
        for j in range(len(YEARS)):
            lookup_year = YEARS[j]
            # check if next point was last year
            if j < len(YEARS)-1:
                year_2 = YEARS[j + 1]
                # lookup_year is int, need to change to str that can be checked in dic
                # find rank and rank for next year: check if lookup_year in dic, otherwise set rank as infinitive
                if str(lookup_year) in name_data[lookup_name]:
                    rank = int(name_data[lookup_name][str(lookup_year)])
                else:
                    rank = float('inf')
                if str(year_2) in name_data[lookup_name]:
                    rank2 = int(name_data[lookup_name][str(year_2)])
                else:
                    rank2 = float('inf')
                # check four condition to draw line
                if rank <= MAX_RANK < rank2:
                    x1 = GRAPH_MARGIN_SIZE + j * x_factor
                    y1 = GRAPH_MARGIN_SIZE + rank * y_factor / MAX_RANK
                    x2 = GRAPH_MARGIN_SIZE + (j + 1) * x_factor
                    y2 = y_over1000
                    title = str(lookup_name) + str(rank)
                elif rank > MAX_RANK >= rank2:
                    x1 = GRAPH_MARGIN_SIZE + j * x_factor
                    y1 = y_over1000
                    x2 = GRAPH_MARGIN_SIZE + (j + 1) * x_factor
                    y2 = GRAPH_MARGIN_SIZE + rank2 * y_factor / MAX_RANK
                    title = str(lookup_name) + ' *'
                elif rank > MAX_RANK and rank2 > MAX_RANK:
                    x1 = GRAPH_MARGIN_SIZE + j * x_factor
                    y1 = y_over1000
                    x2 = GRAPH_MARGIN_SIZE + (j + 1) * x_factor
                    y2 = y_over1000
                    title = str(lookup_name) + ' *'
                else:
                    x1 = GRAPH_MARGIN_SIZE + j * x_factor
                    y1 = GRAPH_MARGIN_SIZE + rank * y_factor / MAX_RANK
                    x2 = GRAPH_MARGIN_SIZE + (j + 1) * x_factor
                    y2 = GRAPH_MARGIN_SIZE + rank2 * y_factor / MAX_RANK
                    title = str(lookup_name) + str(rank)

                # create line and text after check condition
                canvas.create_line(x1, y1, x2, y2, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(x1 + TEXT_DX, y1, text=title, fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

        # set up text for last point
        year_last = YEARS[len(YEARS)-1]
        if str(year_last) in name_data[lookup_name]:
            rank_last = int(name_data[lookup_name][str(year_last)])
        else:
            rank_last = float('inf')
        if rank_last > MAX_RANK:
            x = GRAPH_MARGIN_SIZE + (len(YEARS)-1) * x_factor
            y = y_over1000
            title = str(lookup_name) + ' *'
        else:
            x = GRAPH_MARGIN_SIZE + (len(YEARS)-1) * x_factor
            y = GRAPH_MARGIN_SIZE + rank_last * y_factor / MAX_RANK
            title = str(lookup_name) + str(rank_last)

        canvas.create_text(x + TEXT_DX, y, text=title, fill=COLORS[i % 4], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
