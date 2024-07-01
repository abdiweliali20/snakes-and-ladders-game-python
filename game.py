import random
# Define the board with snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)
# Function to update the position based on dice roll and handle snakes and ladders
def get_position(player, current_position):
    dice_value = roll_dice()
    print(f"Player {player} rolled a {dice_value}")
    new_position = current_position + dice_value
    if new_position > 100:
        new_position = current_position  # Player stays in the same position if roll exceeds 100
        print(f"Player {player} stays at {current_position} as roll exceeds 100")
    if new_position in snakes:
        print(f"Player {player} encountered a snake at {new_position}! Sliding down to {snakes[new_position]}")
        new_position = snakes[new_position]
    elif new_position in ladders:
        print(f"Player {player} found a ladder at {new_position}! Climbing up to {ladders[new_position]}")
        new_position = ladders[new_position]
    return new_position
# Main game loop
def play_game():
    print("Welcome to Snakes and Ladders Game!")
    print("Version: 1.0.0")
    print("Rules:")
    print("1. Initially all the players are at starting position i.e. 0.")
    print("2. Take it in turns to roll the dice. Move forward the number of spaces shown on the dice.")
    print("3. If you land at the bottom of a ladder, you can move up to the top of the ladder.")
    print("4. If you land on the head of a snake, you must slide down to the bottom of the snake.")
    print("5. The first player to get to the FINAL position is the winner.")
    print("6. Hit enter to roll the dice.")
    print("7. Limit the number of players to between 1-4")
    player_count = int(input("Enter the number of players (1-4): "))
    if not 1 <= player_count <= 4:
        print("Invalid number of players. Please restart the game.")
        return
    players = [input(f"Enter the name of player {i+1}: ") for i in range(player_count)]
    positions = {player: 0 for player in players}
    while True:
        for player in players:
            input(f"{player}'s turn. Press Enter to roll the dice.")
            current_position = positions[player]
            new_position = get_position(player, current_position)
            positions[player] = new_position
            print(f"{player} is now at position {new_position}")
            if new_position == 100:
                print(f"Congratulations! {player} wins the game!")
                return
# Start the game
play_game()