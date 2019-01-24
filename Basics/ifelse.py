# if statements
# executes piece of python code inside statement if condition is true

# ------------------------- ERROR ---------------------------
# If statement, without indentation (will raise an error):

a = 33
b = 200

if b > a:
print("b is greater than a") # you will get an error

# -------------------------------------------------------------

# EXAMPLE 1

var1 = 100
# if the variable "var1" is not empty (returns true) then execute block of code in statement
if var1:
   print "1 - Got a true expression value"
   print var1
  
# EXAMPLE 2

a = 33
b = 200
# if variable "b" is greater than "a" execute print inside if statement
if b > a:
  print "b is greater than a"

#--------------------------------------------------------------
#--------------------------------------------------------------

# elif statments
# the elif keyword is python is a way of saying "if the previous conditions were not true, then try this condition"

a = 33
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
# -------------------------------------------------------------
# -------------------------------------------------------------

# else statement
# the else keyword catches anything which isn't caught by the preceding conditions

a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# -------------------------------------------------------------
# -------------------------------------------------------------

# shorthand if, else statements
# if and else statements using one line of code ONLY

# shorthand if
if a > b: print("a is greater than b")
 
# shorthand else
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")


