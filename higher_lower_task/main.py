from random import randint

numb = randint(1, 13)

#main function
for i in range(10):
  
  #Print starting number - only occurs before first guess
  if i == 0:
    print("Starting number: " + str(numb))

  #user input to guess H or L - converts to lower
  guess = input(
    "Input \"H\" if the next number is higher, or \"L\" if the next number is lower.\n"
  )
  guess = guess.lower()
  
  #assigns previous number to previous
  previous = numb
  #print(previous) -> test print every loop to ensure that previous is the previous numb
  numb = randint(1, 13)
  #print(numb) -> test print every loop to ensure that randint is changing
  
  #rerolls numb until numb does not equal previous
  while previous == numb:
    numb = randint(1, 13)
  print("Next number: " + str(numb))
  
  #exit condition after 10th run
  if i == 9:
    print("You win")
    break
    
  #comparator for previous to current numb, followed by user's guess
  #correct guess = continue, wrong guess = exit loop
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
