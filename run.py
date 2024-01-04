import random

def create_and_print_boards(dims):
    player_board = [['O' for _ in range(dims)] for _ in range(dims)]
    computer_board = [['O' for _ in range(dims)] for _ in range(dims)]

    print("Player Board:")
    for row in player_board:
        print(*row)

    print("\nComputer Board:")
    for row in computer_board:
        print(*row)


def main():
    create_and_print_boards(5)

main()