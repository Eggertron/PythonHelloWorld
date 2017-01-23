# this is a comment, it leads with a hash sign
# anything that comes after this hash sign will
# not be interpreted by the python interpreter.

# this is your first program output. it will print
# to the console.
print("Hello World")

# here is an assignment.
s = "Hello World, again"
print(s)
# this time notice how I assigned the
# string of characters into a variable
# 's'.

# let's add an input command to get user
# inputs from the console.
name = input("Enter your name: ")
print("Hello " + name)

# now let's try a loop
# make sure to add the proper indentations
# because python requires it to keep
# blocks of code together.
looping = 7;                            # looping is an integer.
while (looping > 0):                    # this condition will repeat while true.
  print("Hello World " + str(looping))  # converted looping to string as printable.
  looping = looping - 1
# noticed how I started the while loop
# block with the colon and then indented
# the rest of the code that belongs to 
# that loop.

# let's try the if operator
testNumber = 50
if (testNumber > 0):
  print("The test number is greater than zero")

# let's try a nested if statement. This will have
# an if inside and if statement.
if (testNumber > 10):
  print("The test number is greater than ten")
  if (testNumber > 20):
    print("The test number is greater than twenty too!")
    
# notice how the indentation groups the chuncks of code
# to it's appropriate parent line.

# what if you want your input to be accepted as
# something other than a string?
someNumber = int(input("Enter a number: "))
# you see how I used the integer casting function to change
# try and change the string to a number? don't input a non integer!
print("Your number is", someNumber)
# also noticed how i used the print function this time.
