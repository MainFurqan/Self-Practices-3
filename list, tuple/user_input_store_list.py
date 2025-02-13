# Declare a list 
favorite_games = []

# Input from user using loop
print("Enter your Favorite Games:")
for i in range(1, 4):
    game = input(f"No {i}: ")
    favorite_games.append(game)

# Display output
for game in favorite_games:
    print(game)