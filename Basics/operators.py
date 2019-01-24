# Arithmetic Operators
# a = 10, b = 20

# Addition (+)
a + b = 30

# Subtatraction (-)
a - b = -10

# Multiplication (*)
a * b = 200

# Division (/)
b / a = 2

# Modulus (%)
# divides left variable by right variable and returns remainder
b % a = 0

# Exponent (**)
a**b = 10 to the power 20


# --------------------------------------------------------------------------------

# Comparison Operators
# these operators compare the values on either sides of them and decide the relation among them

# (==) if the values of two operands are equal, then the condition becomes true
(a == b) is not true.

# (!=) if values of two operands are not equal, then condition becomes true
(a != b) is true.

# (<>) if values of two operands are not equal, then condition becomes true (similar to !=)
(a <> b) is true

# (>) if the value on left is greater than the value on right, then condition becomes true
(a > b) is not true.

# (<) if the value on left is less than the value on right, then condition becomes true
(a < b) is true.

# (>=) if the value on left is greater than or equal to the value on right, then condition becomes true
(a >= b) is not true.

# (<=) if the value on left is less than or equal to the value on right, then condition becomes true
(a <= b) is true.

# ---------------------------------------------------------------------------------

# Assignment Operators

# (=) assigns values from right side to left side	
c = a + b assigns value of a + b into c

# (+=) adds right variable to the left variable and assigns the result to the left variable 
c += a is equivalent to c = c + a

# (-=) subtracts right variable from the left variable and assign the result to left variable
c -= a is equivalent to c = c - a

# (*=) multiplies right variable with the left variable and assign the result to left variable
c *= a is equivalent to c = c * a

# (/=) divides left variable with the right variable and assign the result to left variable
c /= a is equivalent to c = c / a

# (%=) takes modulus using two variables and assign the result to left variable
c %= a is equivalent to c = c % a

# (**=) power calculation on variables and assigns value to the left variable
c **= a is equivalent to c = c ** a

# ----------------------------------------------------------------------------------------------

# Logical Operators

# (and) if BOTH the variables are true (not empty) then condition becomes true.
(a and b) is true.

# (or) if ANY of the two variables are true (not empty) then condition becomes true.
(a or b) is true.

# (not) used to reverse the logical state
Not(a and b) is false.

# --------------------------------------------------------------------------------------------------

# Membership Operators
# membership operators test for membership in a sequence, such as strings, lists, or tuples
# a = 10, b = 20, list = [1, 2, 3, 4, 5 ];

# (in) true if it finds a variable in the specified sequence and false otherwise
if ( a in list ):
   a is in list
else:
   a is not in list
    
# (not in) true if it does not finds a variable in the specified sequence and false otherwise
if ( b not in list ):
   b is not in list
else:
   b is in list
    
# -----------------------------------------------------------------------------------------------

