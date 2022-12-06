from random import randint

numb = randint(1, 13)

for i in range(10):
  if i == 0:
    print("Starting number: " + str(numb))

  guess = input(
    "Input \"H\" if the next number is higher, or \"L\" if the next number is lower.\n"
  )
  guess = guess.lower()
  previous = numb
  numb = randint(1, 13)
  while previous == numb:
    numb = randint(1, 13)
  print("Next number: " + str(numb))
  if i == 9:
    print("You win")
    break
  if previous > numb:
    if guess == "l":
      pass
    elif guess == "h":
      print("You lose")
      break
  elif previous < numb:
    if guess == "h":
      pass
    elif guess == "l":
      print("You lose")
      break
