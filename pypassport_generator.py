import string
from random import randint, choice, shuffle

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = input('How many letters would you like in your password?\n')
n_symbols = str(input('How many symbols would you like?\n'))
n_num = str(input('How many numbers would you like?\n'))
output_type = input("\"Randomised\" or \"Not Randomised\"?\n").lower()


class password:

  def __init__(self, n_letters, n_symbols, n_num, output_type):
    self.n_letters = n_letters
    self.n_symbols = n_symbols
    self.n_num = n_num
    self.output_type = output_type

  def password(self, n_letters, n_symbols, n_num, output_type):
    pwd = []
    for i in range(int(n_letters)):
      pwd.append(choice(letters))
    for i in range(int(n_symbols)):
      pwd.append(choice(symbols))
    for i in range(int(n_num)):
      pwd.append(randint(0, 9))
    if output_type == "randomised":
      shuffle(pwd)
    pwd = "".join([str(item) for item in pwd])
    print(pwd)
    #def __repr__(self):
    #return repr(self.pwd)


y = password(n_letters, n_symbols, n_num, output_type)

#y is returning either <__main__.password at 0x1c8c9336100> or <__main__.password object at 0x000001C8C9336100>, don't know why. Tried assigning it to self.pwd, pwd, tried using __str__, __repr__, print, no print, cant fix the problem.
#the code works when taken out of the class and run, so not sure how to get it to work in the class
