from random import randint

numb = randint(1, 13)
iterations = 10
print("Starting number: " + str(numb)) #Print starting number - only occurs before first guess


#main function
for i in range(iterations):
  
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
  
  #exit condition after Nth run
  if i == int(iterations)-1:
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
