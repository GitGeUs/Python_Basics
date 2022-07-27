password = "abc"
attampts = 0
attampt_limit = 3
name = input("What is your name: ")

while attampts < attampt_limit:
    entered_pass = input("Please enter your password: ")
    attampts += 1
    if password == entered_pass:
        print("Welcome Back " + name)
        break
else:
        print(name + " You entered wrong password 3 times. Please try in one year again")