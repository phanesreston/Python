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

print "I am " + 25 + " years old."          # gives error (TypeError: cannot concatenate 'str' and 'int' objects)
print "I am " + str(25) + " years old."     # fixes error by converting integer to string using str()

# (%) used to concatenate strings & integers
# %s is used to concatenate string values
name = "Slim Shady"                            # assigns string value "Slim Shady" to variable "name"
print "Hi, my name is %s"%(name)               # outputs string "Hi, my name is Slim Shady"


# -----------------------------------------------------------------------------------

# Standard Print Statement (Python 3)
# (will ONLY work in python 3 or greater)
print ("Hello World!")
