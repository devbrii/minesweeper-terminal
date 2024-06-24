def bees_total(row): # Number of bees varies depending on the size of the board
    if row == 8:
        number_of_bees = 8
        highest_value = 8
    elif row == 12:
        number_of_bees = 15
        highest_value = 12
    else:
        number_of_bees = 25
        highest_value = 16

    return number_of_bees, highest_value


def append_bees(board, row): # Randomly appends all bees in the board
    number_of_bees, highest_value = bees_total(row)
    import random

    counter = 0
    while counter < number_of_bees:
        bees_column = random.randint(1, highest_value)
        bees_row = random.randint(1, highest_value)
        if board[bees_row][bees_column] != "  B  ": # Normally, appending bees in the board will not cause any problems
            board[bees_row][bees_column] = "  B  "
        else: # Except if the cell is already a bee
            board[bees_row][bees_column] = "  B  " # Thus, we just set the cell into a bee
            number_of_bees += 1 # And add 1 so that the number of bees will still be the same. 

        counter += 1


def count_bees(board, row, column, bee): # This appends the number of bees on a cell
    if bee != 0:
        board[row][column] = "  " + str(bee) + "  "

    else:
        board[row][column] = "     "


# Appending the number and spaces in each cell of the board requires iterating its neighbors and manually calculating if a bee is present in the neighboring cells.
# In the code below, all neighboring cells involved in checking is iterated, including the cell that a number or space will be appended.
# This will cause no problem since that cell is empty and no bee will be seen in it, so it is safe to iterate that cell.

# Firstly, cells that are not in the first and last row, as well as first and last column, will be checked.
# It is easier since all neighboring cells occur in three-by-three, thus, no index error will occur.
# The remaining neighboring cells do not occur in three-by-three so the row range and column range are manipulated to prevent the occurrence of index errors.

def count_numbers_inside(board, row, column):
    bee = 0

    curr_row = row - 1
    for x in range(curr_row, curr_row + 3):
        curr_column = column - 1
        for y in range(curr_column, curr_column + 3):
            if board[curr_row][curr_column] == "  B  ":
                bee += 1
            curr_column += 1
        curr_row += 1

    count_bees(board, row, column, bee)


def count_numbers_row_1(board, row, column, last_row_column):
    bee = 0

    if column == 1:
        curr_row = row
        for x in range(2):
            curr_column = column
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    elif column == last_row_column:
        curr_row = row
        for x in range(2):
            curr_column = column - 1
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    else:
        curr_row = row
        for x in range(2):
            curr_column = column - 1
            for y in range(3):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    count_bees(board, row, column, bee)


def count_numbers_last_row(board, row, column, last_row_column):
    bee = 0

    if column == 1:
        curr_row = row - 1
        for x in range(2):
            curr_column = column
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    elif column == last_row_column:
        curr_row = row - 1
        for x in range(2):
            curr_column = column - 1
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    else:
        curr_row = row - 1
        for x in range(2):
            curr_column = column - 1
            for y in range(3):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    count_bees(board, row, column, bee)


def count_numbers_left(board, row, column, last_row_column):
    bee = 0

    if (row != 1) and (row != last_row_column):
        curr_row = row - 1
        for x in range(3):
            curr_column = column
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    count_bees(board, row, column, bee)


def count_numbers_right(board, row, column, last_row_column):
    bee = 0

    if (row != 1) and (row != last_row_column):
        curr_row = row - 1
        for x in range(3):
            curr_column = column - 1
            for y in range(2):
                if board[curr_row][curr_column] == "  B  ":
                    bee += 1
                curr_column += 1
            curr_row += 1

    count_bees(board, row, column, bee)


def append_numbers_and_spaces(board, row):
    if row == 8:
        last_row_column = 8
    elif row == 12:
        last_row_column = 12
    elif row == 16:
        last_row_column = 16

    row = 0
    for x in board:
        column = 0
        for y in board:
            if (row != 0) and (column != 0):
                if board[row][column] == "  B  ":
                    board[row][column] == "  B  "
                else:
                    if (row != 1) and (column != 1) and (row != last_row_column) and (column != last_row_column):
                        count_numbers_inside(board, row, column)
                    elif (row == 1):
                        count_numbers_row_1(board, row, column, last_row_column)
                    elif (row == last_row_column):
                        count_numbers_last_row(board, row, column, last_row_column)
                    elif (column == 1):
                        count_numbers_left(board, row, column, last_row_column)
                    else:
                        count_numbers_right(board, row, column, last_row_column)
            column += 1
        row += 1
