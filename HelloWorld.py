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
