import functions
import os
os.system("cls")

is_running = True
while is_running:
    choice = functions.main_menu()
    if choice == 1:
        functions.play()
        print()
    elif choice == 2:
        functions.instructions()
    elif choice == 0:
        print("Program Terminated")
        print()
        is_running = False
    else:
        print("Invalid Choice! Try Again")
        print()
