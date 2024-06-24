def load_save_successfully(loaded_or_saved): # Message to inform user that board is loaded/saved successfully
    print()
    print(f"Game is successfully {loaded_or_saved}.")
    print()


#FOR BOARD
# Loads a file as the current board
def load_file_board(file_name):
    board = []
    file_handle = open(file_name, "r")
    for line in file_handle:
        data = line.split(",")
        data[-1] = data[-1][0:-1]
        board.append(data)
    file_handle.close()

    return board


# Saves the current game
def save_file_board(file_name, board):
    file_handle = open(file_name, "w")
    for line in board:
        file_handle.write(",".join(line))
        file_handle.write("\n")
    file_handle.close()


# FOR DICTIONARIES
def load_file_dict(file_name):
    dictionary = {}
    file_handle = open(file_name, "r")
    for line in file_handle:
        data = line[0:-1].split("STORE")
        coordinates = data[0]
        cell = data[1]
        dictionary[coordinates] = cell
    file_handle.close()

    return dictionary


def save_file_dict(file_name, dictionary):
    file_handle = open(file_name, "w")
    for line in dictionary:
        file_handle.write(line + "STORE" + dictionary[line] + "\n")
    file_handle.close()



