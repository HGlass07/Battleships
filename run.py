import random

def instructions():
    print("\nWelcome to Battleships\n")
    print("Below you will see your board, with your ships represended by 'S' symbols.\n")
    print("Start by guessing coordinates to try and hit your opponent's ships.\n")
    print("The game ends when either you or the computer sinks all their opponent's ships.\n")


'''generates player and computer opponent boards'''
def create_boards(dims):
    player_board = [['O' for _ in range(dims)] for _ in range(dims)]
    computer_board = [['O' for _ in range(dims)] for _ in range(dims)]

    '''four randomly placed 'ships', represended by 'S' are placed on the player board'''
    for _ in range(4):
        while True:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - 1)
            if player_board[row][col] == 'O':
                player_board[row][col] = 'S'
                break

    '''four randomly placed 'ships', represended by 'S' are placed on the computer board'''
    for _ in range(4):
        while True:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - 1)
            if computer_board[row][col] == 'O':
                computer_board[row][col] = 'S'
                break

    '''player board is printed at the start'''
    print("Player Board:")
    print_board(player_board)

    return player_board, computer_board

'''computer print board function - computer board is printed without showing ship location to player,
ships are only revealed once hit, shown as an "X"'''
def print_computer_board(computer_board):
    hidden_board = [['O' if cell != 'X' else 'X' for cell in row] for row in computer_board]
    print("Computer's Board:")
    for row in hidden_board: 
        print(*row)

'''player print board function'''
def print_board(board):
    for row in board:
        print(*row)

'''coordinate check function ensures coodinate guesses are within valid range'''
def is_valid_coordinate(dims, row, col):
    return 0 <= row < dims and 0 <= col < dims

'''main game function'''
def play_game(dims):
    player_board, computer_board = create_boards(dims)
    player_guessed_coordinates = set()
    computer_guessed_coordinates = set()

    while True:
        '''player turn'''
        print("\nPlayer's Turn")
        while True:
            try:
                player_row_guess = int(input("Enter a row number: "))
                player_col_guess = int(input("Enter a column number: "))
                
                if not is_valid_coordinate(dims, player_row_guess, player_col_guess):
                    print("Invalid coordinates, please guess again.")
                    continue

                '''checks if player has already guessed coordinates'''
                if (player_row_guess, player_col_guess) in player_guessed_coordinates:
                    print("You've already guessed these coordinates, please guess again.\n")
                    continue

                player_guessed_coordinates.add((player_row_guess, player_col_guess))
                break

            except ValueError:
                print("Invalid input. Please enter a valid numeric value.\n")
                continue

        '''checks if player guess hits opponent ship'''
        if computer_board[player_row_guess][player_col_guess] == 'S':
            print("Hit!")
            computer_board[player_row_guess][player_col_guess] = 'X'
        else:
            print("You missed")

        '''prints updated computer board, only hit ships will show'''
        print_computer_board(computer_board)

        '''checks for player win'''
        if all ('S' not in row for row in computer_board):
            print("Well done! You sunk all your opponent's ships and won the game\n")
            break

        '''computer turn'''
        print("\nComputer's Turn")
        while True: 
            computer_row_guess = random.randint(0, dims -1)
            computer_col_guess = random.randint(0, dims -1)

            '''checks if computer has already guessed coordinates'''
            if (computer_row_guess, computer_col_guess) not in computer_guessed_coordinates:
                computer_guessed_coordinates.add((computer_row_guess, computer_col_guess))
                break
        
        '''checks if computer guess hits player ship'''
        if player_board[computer_row_guess][computer_col_guess] == 'S':
            print("Computer hit at coordinates: ({}, {})".format(computer_row_guess, computer_col_guess))
            player_board[computer_row_guess][computer_col_guess] = 'X'
        else:
            print("Computer missed")

        '''prints updated player board, updated with hits if applicable'''
        print("Your board: ")
        print_board(player_board)

        '''checks for computer win'''
        if all ('S' not in row for row in player_board):
            print("The computer sunk all your ships, you lose!\n")
            break

    restart = input("Do you want to play again? (yes/no):\n ")
    if restart.lower() == 'yes':
        play_game(dims)
    else:
        print("Thanks for playing")
    

def main():
    instructions()
    play_game(5)
    
main()
