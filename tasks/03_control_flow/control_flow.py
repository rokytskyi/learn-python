# Task 3: Control Flow
# Complete the exercises below

# 1. Create an if-else statement to check if a number is positive, negative, or zero
# print("Number checker:")
# number = 0  # Try changing this value
# Your code here:


# 2. Write a program that determines if a year is a leap year
# print("\nLeap year checker:")
# Your code here:
# year = 2024  # Try changing this value

# 3. Create a for loop to iterate through a list of items. Print each item
# print("\nFor loop example:")
# Your code here:
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]


# 4. Use a while loop to implement a simple guessing game
# print("\nWhile loop example:")
# Your code here:
# Example:
# import random
# secret_number = random.randint(1, 10)
# guess = 0
# attempts = 0
# 
# print("I'm thinking of a number between 1 and 10.")
# while guess != secret_number and attempts < 3:
#     guess = int(input("Your guess: "))
#     attempts += 1
#     guessing checks here
#
# Output result here

# 5. Implement a nested loop structure
# print("\nNested loop example:")
# Your code here:
# Example:
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"({i}, {j})", end=" ")
#     print()  # New line after each row


# Real-World Task: Adventure Game
# This task will help you apply conditional statements, loops, and logical operators
# in a practical and fun context.

# Game variables
# player_health = 100
# player_score = 0
# game_running = True

# Function to display the game title and instructions
# def display_intro():
#     print("\nADVENTURE GAME: FOREST MYSTERY")
#     print("\nYou find yourself at the edge of a mysterious forest.")
#     print("Your goal is to explore the forest and find the hidden treasure.")
#     print("Be careful with your choices, as they will affect your health and score.")

# Function to display player status
# def display_status():
#     print(f"\nHealth: {player_health}  Score: {player_score}")

# Function for the starting scenario
# def forest_entrance():
#     display_status()
#     print("\nWhat would you like to do?")
#     print("1. Enter the forest")
#     print("2. Walk around the perimeter")
#     print("3. Turn back and go home")
    
#     choice = input("\nYour choice: ")
    
#     if choice == "1":
#         # Enter the forest - go to next scenario
#         return "forest_path"
#     elif choice == "2":
#         # Walk around - different outcome
#         print("\nAs you walk around the perimeter, you find a map!")
#         global player_score
#         player_score += 5
#         return "forest_entrance"
#     elif choice == "3":
#         # Go home - end game
#         print("\nYou decided to play it safe and go home. Adventure over!")
#         return "game_over"
#     else:
#         print("\nInvalid choice. Please try again.")
#         return "forest_entrance"

# Add more scenario functions here
# def forest_path():
#     # Implementation for the forest path scenario
#     pass

# def encounter_animal():
#     # Implementation for the animal encounter scenario
#     pass

# def find_treasure():
#     # Implementation for finding the treasure
#     pass

# Function to check if the game is over
# def check_game_over():
#     global player_health, game_running
#     if player_health <= 0:
#         print("\nYour health has reached zero. Game over!")
#         game_running = False
#         return True
#     return False

# Function to ask if the player wants to play again
# def play_again():
#     response = input("\nWould you like to play again? (yes/no): ")
#     return response.lower() in ["yes", "y"]

# Main game loop
# def main_game():
#     global player_health, player_score, game_running
    
#     # Reset game variables
#     player_health = 100
#     player_score = 0
#     game_running = True
#     current_scenario = "forest_entrance"
    
#     display_intro()
    
#     # Game loop
#     while game_running:
#         # Handle different scenarios based on current_scenario variable
#         if current_scenario == "forest_entrance":
#             current_scenario = forest_entrance()
#         elif current_scenario == "forest_path":
#             current_scenario = forest_path()
#         elif current_scenario == "encounter_animal":
#             current_scenario = encounter_animal()
#         elif current_scenario == "find_treasure":
#             current_scenario = find_treasure()
#         elif current_scenario == "game_over" or current_scenario == "win":
#             break
        
#         # Check if game should end
#         if check_game_over():
#             break
    
#     # Display final score
#     print(f"\nFinal score: {player_score}")
    
#     # Ask to play again
#     if play_again():
#         main_game()
#     else:
#         print("\nThanks for playing!")

# Start the game
# if __name__ == "__main__":
#     main_game()