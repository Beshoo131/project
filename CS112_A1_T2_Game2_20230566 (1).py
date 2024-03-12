# File: CS112_A1_T2_Game2_20230566
# Purpose: Number Scrabble
# Author: AbdelRahman Sherif Mahmoud AboZekri
# ID: 20230566


def number_scrabble():
    available_numbers = list(range(1, 10))
    player1_numbers = []
    player2_numbers = []

    def print_board():
        print(f"Available Numbers: {available_numbers}")
        print(f"Player 1 Numbers: {player1_numbers}")
        print(f"Player 2 Numbers: {player2_numbers}")

    def check_winner(player_numbers):
        if len(player_numbers) >= 3:
            for i in range(len(player_numbers)):
                for j in range(i + 1, len(player_numbers)):
                    for k in range(j + 1, len(player_numbers)):
                        if player_numbers[i] + player_numbers[j] + player_numbers[k] == 15:
                            return True
        return False

    while available_numbers:
        print_board()

        # Player 1's turn
        player1_choice = int(input("Player 1, choose a number: "))
        while player1_choice not in available_numbers:
            print("Invalid choice. Please choose a number from the available numbers.")
            player1_choice = int(input("Player 1, choose a number: "))

        available_numbers.remove(player1_choice)
        player1_numbers.append(player1_choice)

        if check_winner(player1_numbers):
            print_board()
            print("Player 1 wins!")
            break

        print_board()

        # Player 2 turn
        player2_choice = int(input("Player 2, choose a number: "))
        while player2_choice not in available_numbers:
            print("Invalid choice. Please choose a number from the available numbers.")
            player2_choice = int(input("Player 2, choose a number: "))

        available_numbers.remove(player2_choice)
        player2_numbers.append(player2_choice)

        if check_winner(player2_numbers):
            print_board()
            print("Player 2 wins!")
            break

    print_board()
    print("It's a draw!")

# Start the game
number_scrabble()