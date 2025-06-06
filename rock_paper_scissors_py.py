# -*- coding: utf-8 -*-
"""rock_paper_scissors.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XMWBj7wULzS3ezXhcH50IwAW3JogtWS6
"""

import random

print("🎮 Welcome to Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(options)

print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("🎉 You win!")
else:
    print("😢 You lose!")