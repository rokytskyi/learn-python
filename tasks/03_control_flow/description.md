# Task 3: Control Flow

## Objective
Learn how to control the flow of your program using conditional statements and loops.

## Instructions
1. Create an if-else statement to check if a number is positive, negative, or zero
2. Write a program that determines if a year is a leap year
3. Create a for loop to iterate through a list of items
4. Use a while loop to implement a simple guessing game
5. Implement a nested loop structure

## Concepts to Learn
- Conditional statements (`if`, `elif`, `else`)
- Logical operators (`and`, `or`, `not`)
- Comparison operators
- For loops
- While loops
- Loop control statements (`break`, `continue`)
- Nested loops

## Expected Output
```
Number checker:
[Output showing positive/negative/zero check]

Leap year checker:
[Output showing leap year check]

For loop example:
[Output showing iteration through a list]

While loop example:
[Output showing a simple guessing game]

Nested loop example:
[Output showing a pattern or matrix]
```

## Real-World Task: Adventure Game

Create a text-based adventure game where the player navigates through different scenarios by making choices. This task will help you apply conditional statements, loops, and logical operators in a practical and fun context.

### Requirements:
1. Create a game with at least 3 different scenarios/locations
2. Each scenario should present the player with 2-3 choices
3. Use if-elif-else statements to handle different player choices
4. Include at least one loop to allow repeated actions (e.g., trying again after a failure)
5. Implement a scoring or health system that changes based on player choices
6. Create at least one "game over" condition and one "win" condition
7. Use nested conditionals for complex decision paths
8. Include a way to replay the game when it ends

### Verification Criteria:
Your program should:
- Display clear instructions and scenario descriptions
- Accept user input for making choices
- Respond appropriately to different choices using conditional statements
- Track and display the player's score or health
- Use loops to control game flow and allow repeated actions
- Have clear win and lose conditions
- Provide feedback based on the player's choices and current state
- Allow the player to restart the game after completion

### Example Output:
```
ADVENTURE GAME: FOREST MYSTERY

You find yourself at the edge of a mysterious forest.
Health: 100  Score: 0

What would you like to do?
1. Enter the forest
2. Walk around the perimeter
3. Turn back and go home

Your choice: 1

You enter the dark forest. The path splits in three directions.
Health: 100  Score: 10

Which path do you take?
1. The narrow path to the left
2. The overgrown middle path
3. The wide path to the right

Your choice: 2

As you follow the overgrown path, you encounter a wild animal!
Health: 100  Score: 20

What do you do?
1. Try to scare it away
2. Slowly back away
3. Offer it some food from your backpack

Your choice: 3

The animal accepts your food and reveals a hidden treasure behind it!
Health: 100  Score: 50

Congratulations! You've found the forest treasure and won the game!
Final score: 50

Would you like to play again? (yes/no): no

Thanks for playing!
```

## Tips
- A leap year is divisible by 4, but not by 100 unless it's also divisible by 400
- For loops are typically used when you know the number of iterations in advance
- While loops are used when the number of iterations depends on a condition
- The `break` statement exits a loop completely
- The `continue` statement skips the current iteration and moves to the next one
- Be careful with while loops to avoid infinite loops
- Indentation is crucial in Python for defining code blocks
- Use functions to organize your code for different scenarios
- Consider using dictionaries to store game states or scenario information