print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice = input("Is it left or right?\n")
choice = choice.lower()

if choice == "right":
  print("Fall into a hole.\nGame Over.")
  quit()
elif choice == "left":
  choice = input("Swim or wait? \n")
  choice.lower()

if choice == "wait":
  choice = input("Choose a door colour?\n")
  choice.lower()
else:
  print("Attacked by trout.\nGame Over.")
  quit()
door_dict = {
  "red": "Burned by fire.\nGame Over.",
  "blue": "Eaten by beasts.\nGame Over.",
  "yellow": "You Win!"
}

if choice in door_dict:
  print(door_dict[choice])
else:
  print("Game Over.")
