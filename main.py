import random
#lists of characters to randomize
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#ascii art
print('''
  ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"    Password generator by Hottay
  "Y8888888888P"
''')

#variables
num_letters = int(input("Number of letters: \n"))
num_numbers = int(input("Number of numbers: \n"))
num_symbols = int(input("Number of symbols: \n"))
password_list = []
print("Generating your password..")
#letters randomized loop
for i in range(1, num_letters + 1):
    password_list += random.choice(letters)

#numbers randomized loop
for i in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

#symbols randomized loop
for i in range(1, num_letters + 1):
    password_list += random.choice(symbols)

#randomizing the order of characters
random.shuffle(password_list)

#adding the list items into a final string
string = ''.join(password_list)

#final password
print("Password generated!")
print(string)
