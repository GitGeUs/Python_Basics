
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
what = input("What to do: ")

if what == "+":
    print("Result is " + str(num_1 + num_2))

elif what == "-":
    print(num_1 - num_2)

elif what == "*":
    print(num_1 * num_2)

# lets do division using try/except
elif what == "/":
    try:
        div_result = num_1 / num_2
    except ZeroDivisionError:
        print ("you cannot divide by zero")
        div_result = 0
    print(div_result)

# elif what = "//":
#     print(num_1 // num_2)

elif what == "%" or what =="**":
    print("This is simple calculator. Please pay $5 for fully functional version!")

else:
    print("Wrong operation")
