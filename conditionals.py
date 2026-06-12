# is_male = False
# is_tall = True

# if is_male and is_tall :
#     print("you are a tall male")
# elif is_male and not is_tall :
#     print("you are a short male")
# elif not is_male and is_tall :
#     print("you are not a male but you are tall")
# else:
#     print("you are neither a male nor tall")



# num_1 = -86
# num_2 = 55

# if num_1 > num_2 :
#     print(str(num_1) + " is greater than " + str(num_2))
# else:
#     print(str(num_2) + " is grater than " + str(num_1))



username = input("Enter your username :")
password = input("Enter your password :")

if username == "Admin" and password == "1234" :
    print("welcome Admin")
else:
    print("wrong username or password")