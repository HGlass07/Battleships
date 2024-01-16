import random


class Battleships:
    # class constructor
    def __init__(self, dims):
        self.dims = dims
        self.user_board = [['O' for _ in range(dims)]
                           for _ in range(dims)]
        self.comp_board = [['O' for _ in range(dims)] for _ in range(dims)]
        self.user_guess = set()
        self.comp_guess = set()

    # game instructions
    def instructions(self):
        print("\nWelcome to Battleships!\n")
        print("Below you will see your board, with your")
        print("ships represended by 'S' symbols.\n")
        print("Start by guessing coordinates (0-4) to try and hit")
        print("your opponent's ships.\n")
        print("The game ends when either you or the computer sinks")
        print("all their opponent's ships.\n")

    # generates player and computer opponent boards
    # four randomly placed 'ships', represended by 'S' are
    # placed on the player and computer boards
    def create_boards(self):

        self.user_board = [['O' for _ in range(self.dims)]
                           for _ in range(self.dims)]
        self.comp_board = [['O' for _ in range(self.dims)]
                           for _ in range(self.dims)]

        for _ in range(4):
            self.place_ship(self.user_board)

        for _ in range(4):
            self.place_comp_ship()

        print("Player Board:")
        self.print_board(self.user_board)

    # prints player and computer boards
    def place_ship(self, board):
        while True:
            row = random.randint(0, self.dims - 1)
            col = random.randint(0, self.dims - 1)
            if board[row][col] == 'O':
                board[row][col] = 'S'
                break

    def place_comp_ship(self):
        while True:
            row = random.randint(0, self.dims - 1)
            col = random.randint(0, self.dims - 1)
            if self.comp_board[row][col] == 'O':
                self.comp_board[row][col] = 'S'
                break

    def print_board(self, board):
        for row in board:
            print(*row)

    def print_comp_board(self):
        hidden_board = [['O' if cell != 'X' else 'X' for cell in row]
                        for row in self.comp_board]
        print("Computer's Board:")
        self.print_board(hidden_board)

    # coordinate check function ensures guesses are within valid range
    def val_coord(self, row, col):
        return 0 <= row < self.dims and 0 <= col < self.dims

    # main game function
    def play_game(self):
        self.user_guess = set()
        self.comp_guess = set()

        self.create_boards()

        while True:
            # player turn
            print("\nPlayer's Turn")
            while True:
                try:
                    # player enteres coordinate guess
                    # guess undergoes validation
                    user_row_guess = int(input("Enter a row number: "))
                    user_col_guess = int(input("Enter a column number: "))
                    if not self.val_coord(user_row_guess, user_col_guess):
                        print("Invalid coordinates, please guess again.")
                        continue
                    # checks if player has already guessed coordinates
                    if (user_row_guess, user_col_guess) in self.user_guess:
                        print("You've already guessed these coordinates")
                        print("please guess again.\n")
                        continue

                    self.user_guess.add((user_row_guess, user_col_guess))
                    break

                except ValueError:
                    print("Invalid input")
                    print("Please enter a valid numeric value.\n")
                    continue

            # checks if player guess hits opponent ship
            if self.comp_board[user_row_guess][user_col_guess] == 'S':
                print("Hit!")
                self.comp_board[user_row_guess][user_col_guess] = 'X'
            else:
                print("You missed")

            # prints updated computer board, only hit ships will show
            self.print_comp_board()

            # checks for player win
            if all('S' not in row for row in self.comp_board):
                print("Well done! You sunk all your opponent's ships")
                print("and won the game\n")
                break

            # computer turn
            print("\nComputer's Turn")
            while True:
                comp_row_guess = random.randint(0, self.dims - 1)
                comp_col_guess = random.randint(0, self.dims - 1)

                # checks if computer has already guessed coordinates
                if (comp_row_guess, comp_col_guess) not in self.comp_guess:
                    self.comp_guess.add((comp_row_guess, comp_col_guess))
                    break

            # checks if computer guess hits player ship
            if self.user_board[comp_row_guess][comp_col_guess] == 'S':
                print("Computer hit at coordinates: ({}, {})".format
                      (comp_row_guess, comp_col_guess))
                self.user_board[comp_row_guess][comp_col_guess] = 'X'
            else:
                print("Computer missed")

            # prints updated player board, updated with hits if applicable
            print("Your board: ")
            self.print_board(self.user_board)

            # checks for computer win
            if all('S' not in row for row in self.user_board):
                print("The computer sunk all your ships, you lose!\n")
                break

        # option to restart game or quit
        while True:
            restart = input("Do you want to play again? (yes/no):\n ").lower()
            if restart == 'yes':
                self.play_game()
                break
            elif restart == 'no':
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    game = Battleships(5)
    game.instructions()
    game.play_game()


if __name__ == "__main__":
    main()
    