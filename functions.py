import bees_and_numbers
import mechanics
import load_save

def main_menu(): # Function used in the main file
    print("=================================")
    print("||    [1] Play Minesweeper     ||")
    print("||    [2] Instructions         ||")
    print("||    [0] Exit the Game        ||")
    print("=================================")
    print()
    choice = int(input("Select a number: "))
    print()

    return choice


def instructions():
    print('''


==================================================
||                                              ||
||                  SYMBOLS                     ||
||                                              ||
||    *          -  Unopened Cells              ||
||    B          -  Bees / Bombs                ||
||    F          -  Flagged Cell/s              ||
||    *Numbers*  -  How many bees neighbors     ||
||                  a cell                      ||
||    *Spaces*   -  No Neighbors                ||
||                                              ||  
==================================================

==================================================
||                                              ||
||                  MECHANICS                   ||
||                                              ||
||  [1] Click a Cell - You can click any cell   ||
||  except for bombs and flagged cells. If you  ||
||  click a cell that is a bomb, you lose the   ||
||  game                                        ||
||                                              || 
||  [2] Flagging/Unflagging - You can flag any  ||
||  cell as long as it is not revealed nor      ||
||  is already flagged. You also have the       ||
||  option to unflag it.                        ||
||                                              ||
||  [3] You win if you opened all the cells     ||
||  that are not bombs                          ||
||                                              ||
||  [4] Loading/Saving - You always have the    ||
||  option to load a saved game before you      ||
||  choose a board. Note that you CANNOT load   ||
||  a game that does not exist. Save a game     ||
||  first by playing an unloaded file.          ||
||                                              ||
==================================================

    
''')


def user_input(): # Level of difficulty of the minesweeper
    print("Choose a board size.")
    print()
    print("=================================")
    print("||       [1] EASY              ||")
    print("||       [2] INTERMEDIATE      ||")
    print("||       [3] DIFFICULT         ||")
    print("=================================")
    print()
    choice_board_size = int(input("Choice: "))

    return choice_board_size


def size(choice_board_size): # Represent each row and column depending on the difficulty
    if choice_board_size == 1:
        row = 8
        column = 8
    elif choice_board_size == 2:
        row = 12
        column = 12
    elif choice_board_size == 3:
        row = 16
        column = 16

    return row, column


def load_option(): # Option to load a file (will be asked for each time user plays the game)
    print()
    load_input = input("Do you want to load a file? (y/n) ").lower()
    print()

    return load_input


def make_2D_list(row, column): # Creates a 2D list
    board_size = [] # Initializing the board

    c = []
    for x in range(column + 1):
        if len(str(x)) == 1:
            c.append(f"  0{x} ")
        else:
            c.append(f"  {x} ")
    board_size.append(c)

    row_count = 1
    for i in range(row):
        r = []
        if len(str(row_count)) == 1:
            r.append(f"  0{row_count} ")
        else:
            r.append(f"  {row_count} ")
        row_count += 1
        for j in range(column):
            r.append("  *  ")
        board_size.append(r)

    return board_size


def defined_board(board): # Modifies the board into a playable one (converts all elements in the list into strings)
    for row in board:
        border = "|"
        for column in row:
            if column == "*|":
                border += "|"
            else:
                border += column + "|"
        print(border)


def storage(board, store_cells): # Used to store the equivalent coordinates of the board into a dictionary
    # After all bombs and numbers and spaces are placed in the board, all cells are essentially "opened".
    # By storing corresponding coordinates of the board into a separate storage (dictionary), it will prevent the board to be overwritten.
    row = 0
    for board_row in board:
        column = 0
        # For every iteration, row and column will be the key-value pairs of the dictionary
        # while the value will be the actual value on the board
        for board_column in board:
            store_cells[str((row, column))] = board[row][column] # I passed str in the store_cells dictionary in order for me to load it as a string in a file, not as a tuple containing integers
            column += 1
        row += 1


def hide_cells(board): # Hides every element of the board
    row = 0
    for board_row in board:
        column = 0
        for board_column in board:
            if row != 0 and column != 0:
                board[row][column] = "  *  " # Asterisks are used in order to represent hidden cells
            column += 1
        row += 1
    # The values on the board are not overwritten by the asterisks since it is first stored in the store_cells dictionary.


def unhide_cells(board, store_cells): # Unhides cells (When a user clicked a bee/bomb, a board with unhidden cells must be shown)
    row = 0
    for board_row in board:
        column = 0
        for board_column in board:
            if row != 0 and column != 0:
                board[row][column] = store_cells[str((row, column))] # For every iteration, the value given the coordinates of the dictionary replace the corresponding coordinates of the board.
            column += 1
        row += 1

    defined_board(board)


def choices_while_playing(): # Necessary choices in minesweeper
    print("===================================")
    print("||       [1] Click a Cell        ||")
    print("||       [2] Flag                ||")
    print("||       [3] Unflag              ||")
    print("||       [4] Save Progress       ||")
    print("||       [0] Exit the Game       ||")
    print("===================================")
    print()
    play_mine_choice = int(input("Select a Number: "))

    return play_mine_choice


def row_column_input(): # User input for row and column
    # Referring to the previous function:
    # This will be effective only in options 1 through 3 (clicking, flagging, and unflagging a cell)
    # This will not be used in options 4 and 0
    print("===================================")
    row_input = int(input("Select a row: "))
    column_input = int(input("Select a column: "))
    print("===================================")

    return row_input, column_input


def play(): # Actual Minesweeper Game
    while True:
        load_input = load_option() # If a user chose to play, an option to load a saved game will be presented.

        if load_input == "y": # If a user chose to load a game
            print()
            choice_board_size = user_input()
            print()
            if choice_board_size == 1: # Easy
                board = load_save.load_file_board("easy_board.txt")
                store_cells = load_save.load_file_dict("easy_store.txt")
                store_flagged_cells = load_save.load_file_dict("easy_flags.txt")

            elif choice_board_size == 2: # Average
                board = load_save.load_file_board("average_board.txt")
                store_cells = load_save.load_file_dict("average_store.txt")
                store_flagged_cells = load_save.load_file_dict("average_flags.txt")

            elif choice_board_size == 3: # Difficult
                board = load_save.load_file_board("difficult_board.txt")
                store_cells = load_save.load_file_dict("difficult_store.txt")
                store_flagged_cells = load_save.load_file_dict("difficult_flags.txt")
  
            row, column = size(choice_board_size)
            load_save.load_save_successfully("loaded")
            print()
            print()
            print(f"Your board is {row} by {column}.")
            break

        elif load_input == "n": # If a user chose to play a new game
            store_cells = {} # Initializing a storage for the board (mentioned in the function earlier)
            store_flagged_cells = {} # Initializing storage for flagged cells (more on this in mechanics.py module)

            choice_board_size = user_input() # Choose difficulty (Easy, Intermediate, and Difficult)
            row, column = size(choice_board_size) # Generates the number of rows and columns

            board = make_2D_list(row, column) # Creates the 2D List
            bees_and_numbers.append_bees(board, row) # Appends all bees randomly
            bees_and_numbers.append_numbers_and_spaces(board, row) # Appends all numbers or spaces (this depends on how many bees are there as neighbors)
            print()
            print()
            print(f"Your board is {row} by {column}.")
            storage(board, store_cells) # After appending all necessary cells on the board, all information are then stored in the store_cells dictionary using this function
            hide_cells(board) # This hides all cells (note that the cells are just hidden, not overwritten)
            break

        else:
            print()
            print("Wrong Input!")
            print()

    print()
    mechanics.count_flag(store_flagged_cells, row) # Counts how many bees are left (depends in store_flagged_cells dictionary)
    print()
    defined_board(board) # Shows/Updates the current playing board


    # ACTUAL MINESWEEPER GAME
    is_playing = True
    while is_playing: # While user is still playing
        number_of_opened_cells, total = mechanics.player_wins(board, row, store_cells) # Refer to mechanics.py module

        if (number_of_opened_cells == total): # Checks if the condition is true, then terminates the program if condition is met.
            mechanics.message()
            defined_board(board) # Prints the board for the last time
            print()
            break # Redirects us to main menu

        # print()
        # print(store_cells) # To check corresponding dict cells in board
        
        # print()
        # print(store_flagged_cells) # To check all flagged cell

        print()
        play_mine_choice = choices_while_playing() # click, flag, unflag, save, or terminate the program
        print()

        if play_mine_choice == 1: # Clicking a board cell
            row_input, column_input = row_column_input()
            print()
            if (row_input == 0) or (column_input == 0):
                print("Invalid Choice!") # You cannot click them because they just serve as a legend
                print()
                mechanics.count_flag(store_flagged_cells, row)
                defined_board(board)
                print()
            else:
                if (store_cells[str((row_input, column_input))] != "  B  ") and (store_cells[str((row_input, column_input))] != "     "): # A number is clicked (in reference to store_cells dict)
                    if (board[row_input][column_input] == "  F  ") or (board[row_input][column_input] != "  *  "): # If a board cell is flagged or is already opened/revealed
                        print()
                        mechanics.already_clicked_flagged(board, row_input, column_input) # Function which states that it is invalid
                    else:
                        print()
                        mechanics.click_cell(board, store_cells, row_input, column_input) # Reveal the cell
                    print()
                    mechanics.count_flag(store_flagged_cells, row)
                    defined_board(board)
                    print()
                elif (store_cells[str((row_input, column_input))])== "     ": # A cell with no neighbor is clicked
                    if (board[row_input][column_input] == "  F  ") or (board[row_input][column_input] != "  *  "): # If a board cell is flagged or is already opened/revealed
                        print()
                        mechanics.already_clicked_flagged(board, row_input, column_input) # Function which states that it is invalid
                    else:
                        print()
                        mechanics.flood_fill(board, store_cells, store_flagged_cells, row_input, column_input, []) # Reveal all cells that are spaces accordingly (suing floodfill algorithm)
                    print()
                    mechanics.count_flag(store_flagged_cells, row)
                    defined_board(board)
                    print()
                elif (store_cells[str((row_input, column_input))]) == "  B  ": # A bomb is clicked (in reference to store_cells dict)
                    if board[row_input][column_input] == "  F  ": # User is unable to click a flagged cell
                        print()
                        mechanics.already_clicked_flagged(board, row_input, column_input)
                        mechanics.count_flag(store_flagged_cells, row)
                        print()
                        defined_board(board)
                        print()
                    else:
                        print()
                        mechanics.click_cell_bomb(row_input, column_input) # Game is over
                        print()
                        unhide_cells(board, store_cells) # Overwrites board cells with stored cells
                        print()
                        is_playing = False # Terminates the program
                    
        elif play_mine_choice == 2: # Flagging a board cell
            row_input, column_input = row_column_input()
            print()
            if (board[row_input][column_input] == "  F  ") or (board[row_input][column_input] != "  *  "):  # If a board cell is flagged or is already opened/revealed
                mechanics.already_clicked_flagged(board, row_input, column_input) # User is unable to flag a cell
                print()
            else: # User wishes to flag a cell that is not revealed (asterisk)
                mechanics.flag(board, store_cells, row_input, column_input, store_flagged_cells) # the coordinate of the board cell is stored in another dictionary, and is replaced by "F"
                print()
            mechanics.count_flag(store_flagged_cells, row)
            defined_board(board)
            print()

        elif play_mine_choice == 3: # Unflagging a board cell
            row_input, column_input = row_column_input()
            print()
            mechanics.unflag(board, store_cells, row_input, column_input, store_flagged_cells) # Unflags the cell (depending on certain conditions --> Refer to the function in the module)
            print()
            mechanics.count_flag(store_flagged_cells, row)
            defined_board(board)
            print()

        elif play_mine_choice == 4: # Saving current game
            if row == 8: # If current game is 8x8
                load_save.save_file_board("easy_board.txt", board)
                load_save.save_file_dict("easy_store.txt", store_cells)
                load_save.save_file_dict("easy_flags.txt", store_flagged_cells)
            elif row == 12: # If current game is 12x12
                load_save.save_file_board("average_board.txt", board)
                load_save.save_file_dict("average_store.txt", store_cells)
                load_save.save_file_dict("average_flags.txt", store_flagged_cells)
            elif row == 16: # If current game is 16x16
                load_save.save_file_board("difficult_board.txt", board)
                load_save.save_file_dict("difficult_store.txt", store_cells)
                load_save.save_file_dict("difficult_flags.txt", store_flagged_cells)
            load_save.load_save_successfully("saved")
            print()
            mechanics.count_flag(store_flagged_cells, row)
            defined_board(board)
            print()

        elif play_mine_choice == 0: # User wishes to terminate the program
            exit_game =  input("Do you really want to exit the game? (y/n) ").lower()
            if exit_game == "y": # Brings us back to main menu
                print()
                print("Redirecting to Main Menu.")
                print()
                break 
            elif exit_game == "n": # Returns to the current board
                print()
                mechanics.count_flag(store_flagged_cells, row)
                defined_board(board)
                print()
            else:
                print()
                print("Invalid choice")
                print()
                mechanics.count_flag(store_flagged_cells, row)
                defined_board(board)
                print()
        else:
            print("Invalid Choice!")


