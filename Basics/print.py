# Standard Print Statement (
# (will not work in python 3 or greater)

# Strings
print "Hello World!"                        # outputs string "Hello World!"

# Integers
print 25                                    # outputs integer "25"
print 2*2                                   # outputs integer "4"
print 2 + 5 + 9                             # outputs integer "16"

# Print Operators
# -------------------------------------------
# (,) used to print multiple strings in a line
print "Hello","World!"                      # outputs string "Hello World!"
print 1,2,3,4,5,6,7,8,9,0                   # outputs multiple integers "1 2 3 4 5 6 7 8 9 0"

# (+) used to concatenate two strings into single string (NO INTEGERS)
print "Hello"+"World"                       # outputs string "HelloWorld" (no space)
print "Hello"+" World"                      # outputs string "Hello World" (with space)
print "20 " +  "+" +  " 2" + " = " + "22"   # outputs string "20 + 2 = 22"

print "I am " + 46 + " years old."          # gives error (TypeError: cannot concatenate 'str' and 'int' objects)
print "I am " + str(46) + " years old."     # fixes error by converting integer to string using str()

# (%) used to concatenate strings & integers
# %s is used to concatenate string values
name = "Slim Shady"                         # assigns string value "Slim Shady" to variable "name"
print "Hi, my name is %s"%(name)            # outputs string "Hi, my name is Slim Shady"

# %d is used to concatenate integer values
age = 46                                    # assigns integer value "46" to variable "age"
print "I am %d years old"%(age)             # outputs string "I am 46 years old"

# %f Used to print floating point integers (decimals)
# %.1f outputs number to 1 decimal place & %.2f to 2 decimal places etc..
pi = 3.1415926
print "pi to 1 decimal place: %.1f "%(pi)
print "pi to 2 decimal places: %.2f "%(pi)
print "pi to 3 decimal places: %.3f "%(pi)
# etc ...

# using %s, %d and %f all together
name = "Bill Gates"
company = "Microsoft"
year = 1975
net = 96.4

print "Hi, my name is %s. I founded my company %s in %d and im now worth %.1f billion dollars"%(name,company,year,net)
# outputs "Hi, my name is Bill Gates. I founded my company Microsoft in 1975 and im now worth 96.4 billion dollars"


# ----------------------------------------------------------------------------------------------------
# ------------------------------------------ PYTHON 3 ------------------------------------------------
# ----------------------------------------------------------------------------------------------------

# Standard Print Statement (Python 3)
# (will ONLY work in python 3 or greater)
print ("Hello World!")
