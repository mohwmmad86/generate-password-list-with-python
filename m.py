#password list
# @mohwmmad86
import random
num = int(input("how many password do you want?"))
# @mohwmmad86
for i in range (num):
    with open("password_list.txt", "a") as file:
        a ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%"
        m = ''.join(random.choice(a) for i in range(0, 10))
        file.write(f"{m}\n")

# github.com/mohwmmad86