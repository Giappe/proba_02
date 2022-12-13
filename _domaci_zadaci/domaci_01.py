import random

# Vezba: 5

# x = int(input("Unesite broj: "))


# print("Tens: ", x // 10)
# print("Fives: ", (x % 10) // 5)
# print("Two's: ", ((x % 10) % 5) // 2)
# print("Ones: ", (((x % 10) % 5) % 2) // 1)

# ----------------------------------------------

# Vezba: 6

# x = int(input("Unesite broj: "))
# deljelnje = x % 2

# if deljelnje == 0:
#     print("Number is even: ", True)
# else:
#     print("Number is even: ", False)

# ----------------------------------------------

# x = int(input('Unesite broj: '))
# computer_number = random.randint(1, 10)

# print("Your number: ", x)
# print("Computer number: ", computer_number)
# if x == computer_number:
#     print("Hit:", True)
# else:
#     print("Hit: ", False)

# ----------------------------------------------

# Vezba: 8

# proj_x = 0
# wall_x = 100
# proj_spd = 20

# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd
# print("Hit: ", proj_x > wall_x)
# proj_x += proj_spd

# ----------------------------------------------

# vezba: 9

# x = 13
# y = int(input("Unesite godine: "))

# print("Allowed -", x <= y)

# ----------------------------------------------

# vezba: 10

db_username = "Peter"
db_password = "123"

username = input("Unesite username: ")
password = input("Unesite lozinku: ")

print(db_username == username and db_password == password)