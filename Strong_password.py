import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to MYPassword Generator")
pw_letter = int(input("How many letters would you like in your Password: \n"))
pw_number = int(input("How many numbers would you like in your Password: \n"))
pw_symbols = int(input("How many symbols would you like in your Password: \n"))

# password = ""
# for char in range(1, pw_letter+1):
#     random_pw = random.choice(letters)
#     password += random_pw
#
# for i in range(1, pw_number+1):
#     password += random.choice(numbers)
#
# for ch in range(1, pw_symbols+1):
#     password += random.choice(symbols)
#
# print(password)

password_list = []
for char in range(1, pw_letter+1):
    random_pw = random.choice(letters)
    password_list.append(random_pw)

for i in range(1, pw_number+1):
    password_list += random.choice(numbers)

for ch in range(1, pw_symbols+1):
    password_list += random.choice(symbols)
random.shuffle(password_list)


password = ""
for char in password_list:
    password += char
print(f"Your Password is: {password}")
