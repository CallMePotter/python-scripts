from random import randint

file = open("list.txt", "r").readlines()
password = ""

words = input("Enter the number of words in password(default 6): ")
if words == "":
    words = 6

passwords = input("Enter the number of passwords(default 10): ")
if passwords == "":
    passwords = 10

print("----------------------------------------------")

for i in range(int(passwords)):
    for j in range(int(words)):
        password += file[randint(0, 999)].rstrip("\n") + " "
    print(str(i + 1) + ". " + password)
    password = ""

print("----------------------------------------------")
