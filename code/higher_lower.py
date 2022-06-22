from art import logo, vs
from game_data import data
import random

print(logo)
def random_data():
  return random.choice(data)

def game():
  A = random_data()
  B = random_data()
  point = 0
  game_should_continue = True
  
  while game_should_continue:
    A = B
    B = random_data()

    while A == B:
      B = random_data()
      print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
      print(vs)
      print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
      guess = (input("Who has higher number of Instagram followers (A or B): ")).lower()
    
      if guess == "a":
        if A['follower_count'] > B['follower_count']:
          point += 1
          print(f"You are right! Points: {point}.\n\n")
        else:
          game_should_continue = False
          print(f"You are Wrong! Total Points: {point}.")
      elif guess == "b":
        if A['follower_count'] < B['follower_count']:
          point += 1
          print(f"You are right! Points: {point}.\n\n")
        else:
          game_should_continue = False
          print(f"You are wrong! Total Points: {point}.")

game()
