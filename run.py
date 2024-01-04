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
                player_board[row][col] = '*'
                break

    """four randomly placed 'ships', represended by '*' are placed on the computer board"""
    for _ in range(4):
        while True:
            row = random.randint(0, dims - 1)
            col = random.randint(0, dims - 1)
            if computer_board[row][col] == 'O':
                computer_board[row][col] = '*'
                break
            
    """player board is printed at the start"""
    print("Player Board:")
    for row in player_board:
        print(*row)



def main():
    instructions()
    create_boards(5)

main()