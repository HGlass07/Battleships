import random

def instructions():
    print("Welcome to Battleships\n")
    print("Below you will see you board, with your ships represended by '*' symbols\n")
    print("Start by guessing a coordinate to try and hit your opponent's ships\n")


"""generates player and computer opponent boards"""
def create_boards(dims):
    player_board = [['O' for _ in range(dims)] for _ in range(dims)]
    computer_board = [['O' for _ in range(dims)] for _ in range(dims)]

    """four randomly placed 'ships', represended by '*' are placed on the player board"""
    for _ in range(4):
        while True:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - 1)
            if player_board[row][col] == 'O':
                player_board[row][col] = 'S'
                break

    """four randomly placed 'ships', represended by '*' are placed on the computer board"""
    for _ in range(4):
        while True:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - 1)
            if computer_board[row][col] == 'O':
                computer_board[row][col] = 'S'
                break

    """player board is printed at the start"""
    print("Player Board:")
    for row in player_board:
        print(*row)

    return player_board, computer_board


def play_game(player_board, computer_board):
    x_coord = input("Please select an x coordinate between 0 and 4")
    y_coord = input("Please select an x coordinate between 0 and 4")
    player_guess = x_coord + y_coord

    if player_guess == 'S' in computer_board:
        print("Hit!")
    else:
        print("You missed")
   
    comp_x_coord = random.randint(0, 4)
    comp_y_coord = random.randint(0, 4)
    computer_guess = comp_x_coord + comp_y_coord

    if computer_guess == 'S' in player_board:
        print("You've been hit!")
    else:
        print("Your opponent missed")



def main():
    instructions()
    create_boards(5)
    

main()