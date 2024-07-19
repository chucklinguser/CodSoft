import random
import string

def generate_password(length, complexion):
    if complexion == 1:
        chars = string.ascii_letters
    elif complexion == 2:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars)
for i in range(length))
    return password

length = int(input("Enter the desired length of the password: "))
print("Choose complexion level: ")
print("1: Lowercase and uppercase letters")
print("2: Letters and digits")
print("3: Letters, digits, and special characters")
complexion = int(input("Enter the complexion level of your password (1-3): "))

password = generate_password(length, complexion)
print("Generated Password:", password)
