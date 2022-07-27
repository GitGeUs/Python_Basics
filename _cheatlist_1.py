
# Pycharm shortcuts
# ctr + /  == comment
# ctr + d  == duplicate line

aa = -2.7
bb = "Welcome to NYC"

print(round(aa))
print(abs(aa))  # returns an absolute value
print (bb.lower())
# print (bb.upper())
# print (bb.find("t")) #position of first "t"
# print (bb.replace("to", "from"))
# print ("lcom" in bb) # prints True/False


cc = [2, 3, 4, 5, 8, 9]
cd = [2, "tom", True, 7, [55,56,57]]
cr = [[1, 2, 3], [11, 22, 33], ["john", "banana", True, 777, "a11"]]

# []list. ()tuples. {}sets. {key:value}dictionaries.
# Lists are ordered, changeable, and allow duplicate. List items are indexed. The first item has index [0], the second item has index [1] etc.
# Tuples are ordered, unchangeable, and allow duplicate. List items are indexed. The first item has index [0], the second item has index [1] etc.
# Tuples are like lists, but immutable(unchangeable), so you can't change them once you created tuple.
# Sets are unordered, unchangeable, and do not allow duplicate. Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Dictionaries are ordered (from python 3.7), changeable and do not allow duplicates.


# Access List Items
#
# print(cc)
# print(cc[2])
# print(cc[0:2]) # slices
# print(cc[:2])
# print(cc[1:])
# print(cc[:]) shallow-copy of cc. Almost the same as print[cc], but not always (google for more info)
# print(cc[-3:-1])
#
# print(cd[1])
# print(cd[4])
#
# print(cr[1][0]) # access list inside list. in our case first item of second list is 11.
# print(cr[2][4])


db = ["John", "Ross", "Tom", "Adam"]
dc = [2, 3, 4, 5, 8, 9]
dd = [2, "tom", True, 7, [55,56,57]]
dr = [[1, 2, 3], [11, 22, 33], ["john", "banana", True, 777, "a11"]]

# Change List items
#
# dd[1] = "ron" # Change Item Value. Instead of "tom" we have "ron" now
# dd[0:3] = "Ann", "Kate", "Jane" # Change a Range of Item Values.
# dd[0:3] = "Ann", "Kate" # If you insert more or less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly: will be deleted or added.
# print(dd)

# dc.append(1)  # appends to the end
# dc.insert(1,8)  # first number is index(position), second - object
# dc.insert(-1,"bob")
# dc.extend(dd)  # adds list dd to list dc. Can add any iterable object (list, tuples, sets, dictionaries etc.)
# dt = db + dc  # easiest way to join two lists. We create new dt list.
# dc.clear()  # removes all items in the list
# dc.remove(4)  # removes by value. In our case 4.
# dc.pop(1)  # removes by index. In our case second item:
# dc.pop()  # If you do not specify the index, the pop() method removes the last item.
# print(dc)

# Alternatively you can remove item from list this way. The del keyword also removes the specified index.
# del dc[1] # remove an item from a list by its index.
# del dc[1:4] # del also supports slices
# del dc # deletes entire variable

# Sort Lists
# db.sort()  # Sort the list alphabetically or numerically, but not
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
# To perform a case-insensitive sort of the list, use str.lower as a key function
# db.sort(key = str.lower)  # Case insensitive sorting.
# db.sort(reverse = True)  # Sort descending.
# db.reverse()  # Prints in reverse order.
# .reverse() is different from .sort(reverse = True), because first prints just in reverse order, while second - sorts.
# print(db)

# Copy of List
# You can't copy a list simply by typing aa2 = aa1, because: aa2 will only be a reference to aa1, and changes made in aa1 will automatically also be made in aa2.
# Instead we can copy list with the copy() method or list() method.
# db2 = db.copy()
# dc2 = list(dc)
# print(db2)
# print(dc2)


# print(db.count("Tom"))  # Prints the number of times the value "Tom" appears in the db list:
# print(len(dc))  # print the number of items in the list
# print(type(dc))


# check id there is "tom in list "cd"
if "tom" in cd:
  print("Yes, 'tom' is in this list")
# check id there is 7 in list "cc"
if 7 in cc:
    print("Yes, 7 is in this list")
else:
    print("7 isn't in this list")



# Range
numbers = range(7)
print (numbers)
# result will be - "range(0, 7)" , not the actual numbers from 0 to 6.

# instead we can use for loop.
for number in numbers:
  print(number)

# Or simply:
for x in range(7):
  print(x)

# Note that range(7) is not the values of 0 to 7, but the values 0 to 6.
for x in range(2, 6):
  print(x)
# means values from 2 to 6 (but not including 6):

# Range with Increment Parameter
for x in range(4, 34, 3):
  print(x)

# Else in For Loop
for x in range(7):
  print(x)
else:
  print("Finally finished!")
# Print all numbers from 0 to 6, and print a message when the loop has ended.

# We can stop executing loop with "break" statement.
for x in range(7):
  if x == 3: break
  print(x)
# It will print 0, 1, 2 and stops

# Pass Statement
for x in [0, 1, 2, 3, 4, 5, 6]:
  pass
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.




# Functions
def func_1():
    print(555)
func_1()

# Function Parameters and Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def func_2(name, surname):
  print(name + " " + surname)
func_2("Jimsher", "Dadiani")

# If your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def func_3(*cars):
  print("Today I use " + cars[2])
func_3("BMW", "Mercedes", "Lexus")

# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def func_4(color1, color2, color3):
  print(color1 + " bulb has left the chat")
func_4(color1 = "Yellow", color2 = "Red", color3 = "Green")

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def func_5(**student):
  print("Best student is " + student["surname"])
func_5(name = "John", surname = "Smith")

# Passing a List as an Argument

def func_6(cars):
  for x in cars:
    print(x)
audi = ["S2", "rs3", "a6", "sq8"]
func_6(audi)

# To let a function return a value, use the return statement.

def func_7(xx):
  return xx / 11
print(func_7(44))
print(func_7(22))
print(func_7(33))


















