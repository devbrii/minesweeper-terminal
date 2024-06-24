import bees_and_numbers
import functions

# If cell is already clicked or flagged
def already_clicked_flagged(board, row_input, column_input):
    if (board[row_input][column_input] == "  F  "): # A board cell is flagged
        print()
        print("That cell is already flagged.")
        print()
        print()
    elif board[row_input][column_input] != "  *  ": # A board cell is already revealed
        print()
        print("That cell is already revealed.")
        print()
        print()


# If a user clicked a cell -
# that is not a bomb:
def click_cell(board, store_cells, row_input, column_input):
    # Depending on the row and column input of the user:
    # Fetches the key-value pair of store_cells and overwrites the corresponding coordinate of the board
    value = store_cells[str((row_input, column_input))]
    board[row_input][column_input] = value


# that is a bomb:
def click_cell_bomb(row_input, column_input):
    print("You have failed!")
    print()
    print(f"Coordinate ({row_input}, {column_input}) is a bomb")
    print()


# that is a space
def flood_fill(board, store_cells, store_flagged_cells, row_input, column_input, cells_visited):
    # check if the coordinate is found in store cells
    if (str((row_input,column_input))) not in store_cells:
        return
    
    # check if the coordinate is already visited
    elif (row_input,column_input) in cells_visited:
        return
    
    # check if the coordinate is flagged
    elif (str((row_input,column_input))) in store_flagged_cells:
        return
    
    value = store_cells[str((row_input, column_input))]
    board[row_input][column_input] = value
    # appends currrent coordinate in cells_visited to avoid repetition
    cells_visited.append((row_input,column_input))
    
    # check if there are no neighboring bees/bombs
    if store_cells[str((row_input,column_input))] != "     ":
        return
    
    flood_fill(board, store_cells, store_flagged_cells, row_input, column_input-1, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input, column_input+1, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input-1, column_input, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input+1, column_input, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input+1, column_input+1, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input-1, column_input-1, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input+1, column_input-1, cells_visited)
    flood_fill(board, store_cells, store_flagged_cells, row_input-1, column_input+1, cells_visited)


# If a user flagged a cell:
def flag(board, store_cells, row_input, column_input, store_flagged_cells):
    # Before putting a flag in the board, the value of the chosen coordinate in the store_cells dictionary
    # (the same as the coordinate in the board) is put first in a dictionary designated only for flagged cells.
    store_flagged_cells[str((row_input, column_input))] = store_cells[str((row_input, column_input))]
    board[row_input][column_input] = "  F  "


# If a user unflagged a cell:
def unflag(board, store_cells, row_input, column_input, store_flagged_cells):
    if board[row_input][column_input] != "  F  ": # The user cannot unflag a board cell that is not flagged in the first place
        print()
        print("Invalid choice!")
        print()
    else: # The process is just the reverse of flagging a cell.

        # store_flagged_cells[row_input, column_input] = store_cells[row_input, column_input]

        del store_flagged_cells[str((row_input, column_input))] # The flagged cell is deleted from the dictionary
        board[row_input][column_input] = "  *  " # Board cell is changed back into a hidden cell (asterisk)


# For number of bees left / numbers of flags placed
def count_flag(store_flagged_cells, row):
    total_number_of_bees, highest_value = bees_and_numbers.bees_total(row) # The total number of bees varies on each sizes

    final_number = total_number_of_bees - len(store_flagged_cells)

    print("========================================")
    print(f"||   Number of BEES / BOMBS left: {final_number}   ||")
    print("========================================")
    print()
    
    # The variable final_number does not actually refer to the number of bees left, but is a result of the modified length of store_flagged_cells
    # This depends on how many flagged cells exists in the playing board
    # A user may flag cells that is more than the number of bees, resulting to a negative value for the final number


# End game if player wins
def player_wins(board, row, store_cells):
    # The condition for winning (involves number_of_opened_cells and total) is in the functions.py module

    number_of_bees, highest_value = bees_and_numbers.bees_total(row)
    number_of_opened_cells = 0 # Initializing the number of opened cells in the board
    number_of_legends = 0  # These are the cell coordinates that are only for references/legends (not included in the minesweeper game; cannot be clicked)
    
    board_row = 0
    for i in board:
        board_column = 0
        for j in board:
            if (board_row != 0) and (board_column != 0):
                if (board[board_row][board_column] == "  F  "):
                    if (store_cells[str((board_row, board_column))] != "  B  "):
                        number_of_opened_cells -= 1
                    else:
                        number_of_opened_cells += 0
                elif (board[board_row][board_column] != "  *  "):
                    number_of_opened_cells += 1
            else:
                number_of_legends += 1
            board_column += 1
        board_row += 1

    total = len(store_cells) - number_of_legends - number_of_bees
    # If the total is calculated, this must equal to the required number of cells that must be opened
    # (note that the bees must not be clicked and the legends are already revealed)
    # To check its validity, it is recommended to uncomment the following:

    # print("store_cells: ", len(store_cells)) # For checking only
    # print("number of opened cells: ", number_of_opened_cells) # For checking only
    # print("number of bees: ", number_of_bees) # For checking only
    # print("number of legend: ", number_of_legends) # For checking only
    # print("total: ", total) # For checking only
    
    return number_of_opened_cells, total # The number of opened cells must equal the total in order to win the game


def message():
    print()
    print()
    print("==========================================================")
    print("||         CONGRATULATIONS! YOU WON THE GAME!           ||")
    print("==========================================================")
    print()
    print()