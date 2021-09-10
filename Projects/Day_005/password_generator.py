#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Initialize the easy password with an empty string
easy_pass =''

for letter in range(nr_letters):
    easy_pass += random.choice(letters)

for symbol in range(nr_symbols):
    easy_pass += random.choice(symbols)

for number in range(nr_numbers):
    easy_pass += random.choice(numbers)
print(f"Your easy password is: {easy_pass}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


hard_pass = []
#Generate random letters, symbols, and numbers

for leta in range(nr_letters):
    hard_pass.append(random.choice(letters))

for symb in range(nr_symbols):
    hard_pass.append(random.choice(symbols))

for num in range(nr_numbers):
    hard_pass.append(random.choice(numbers))


#print(hard_pass)
random.shuffle(hard_pass)
#print(hard_pass)

password = ""
for char in hard_pass:
  password += char

print(f"Your password is: {password}")

# Alternative Approach

#Generate random letters, symbols, and numbers
rand_letters = [random.choice(letters) for i in range(nr_letters)]
rand_symbols = [random.choice(symbols) for i in range(nr_symbols)]
rand_numbers = [random.choice(numbers) for i in range(nr_numbers)]

#Combine together
rand_letters.extend(rand_symbols)
rand_letters.extend(rand_numbers)
#shuffle the list randomly
random.shuffle(rand_letters)
#Convert list to str with ''.join() and print
print(f"Your password is: {''.join(rand_letters)}")