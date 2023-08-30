from prettytable import PrettyTable
import random
import time

print("\n*** Password Generator App ***")

x = PrettyTable()

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
no_of_passwords = int(input("\nHow many passwords you want to generate? "))
password_dict = {}
password_length = int(input("\nEnter length of password: "))
count = 1

while count <= no_of_passwords:
    password = ""
    for i in range(1, password_length + 1):
        password += random.choice(characters)
    password_dict[count] = password
    count += 1

print("\nGenerating entire list........")
time.sleep(2)

x.field_names = ["Generated Passwords"]

for key, value in password_dict.items():
    x.add_row([f"{key} | {value}"])

print(x)

with open("password.txt", "w") as file:
    [file.write(f"{i}----{j}\n") for i, j in password_dict.items()]