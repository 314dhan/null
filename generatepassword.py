import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
def generate_password(length):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password = generate_password(10)
print("Password yang dihasilkan adalah:", password)
