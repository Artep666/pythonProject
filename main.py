import random

your_input = input("Enter a choice (r = rock, p = paper, s = scissors): ")
user = ""
if your_input.lower() == "r":
    user = "rock"
if your_input.lower() == "p":
    user = "paper"
if your_input.lower() == "s":
    user = "scissors"

possible = ["rock", "paper", "scissors"]
computer = random.choice(possible)

print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock, You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
