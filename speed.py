# km/h to mph speed convertor
import re

speed = input("Enter speed: ")
if not re.match("[0-9]", speed):
    print("Error! Only numbers 0-9 allowed!")
    quit()

if len(speed) > 5:
    print ("Error! Only 5 characters allowed!")
    quit()

measure = input("'k' for km/h or 'm' for mph?: ")

if measure.lower() == "k":
    bb = int(speed) / 1.609
    bb_rounded = round(bb, 1)
    print("Your speed in miles is " + str(bb_rounded))
elif measure.lower() == "m":
    cc = int(speed) * 1.609
    cc_rounded = round(cc, 1)
    print("Your speed in kilometers is " + str(cc_rounded))
else:
    print("Wrong input")


