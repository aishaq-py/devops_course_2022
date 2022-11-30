from random import randint
from random import choice


#rand_7
def rand_7():
  choice = randint(1, 10)
  print(choice)
  if choice == 7:
    print("Lucky.")
  else:
    print("Unlucky.")


#rand_1000
def rand_1000():
  num = randint(1, 1000)
  print(num)
  if num % 2 == 1:
    print("Odd.")
  else:
    print("Even.")


#rand_fruit
def rand_fruit():
  food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])
  print(food)
  if food == 'apple' or food == 'grape':
    print('Fruit.')
  elif food == 'bacon' or food == 'steak':
    print('Meat.')
  else:
    print('Yuck.')


#return day
def return_day():
  num = input("Insert day number: ")
  num = int(num) - 1
  days = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Saturday'
  ]
  if num <= 7 and num > 0:
    print(days[num])
  else:
    return None


#list_manipulation
def list_manipulation(_list, _cmd, _loc, _val):
  _cmd = _cmd.lower()
  _loc = _loc.lower()
  if _cmd == "remove":
    if _loc == "end":
      return _list.pop(-1)
    elif _loc == "beginning":
      return _list.pop(0)
  elif _cmd == "add":
    if _loc == "beginning":
      _list = _list.insert(0, _val)
    elif _loc == "end":
      _list = _list.append(_val)
    return _list