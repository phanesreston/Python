# Variable Declaration
# (will work in all versions of python)

# Assigning values to variables
i = 10                          # assigns integer value "10" to variable "i"
f = 2.5                         # assigns floating point (decimal) value "2.5" to variable "f"
s = "John"                      # assigns string value "John" to variable "s"

# Multiple variable assignment
a = b = c = 1                   # assigns value "1" to all three variables (a,b & c)
a, b, c = 1, 2, "John"          # assigns value "1" to variable "a", value "2" to variable "b" & value "John" to variable "c"

# ---------------------------------------------

# Variable data types

# Numbers
var = 1                         # integer value
var = 5.5                       # floating point (decimal) value

# Strings
var = "Hello World!"            # string value

print (var)                     # prints complete string:"Hello World!"
print (var[0])                  # prints first character of the string: "H"
print (var[2:5])                # prints characters starting from 3rd to 5th: "llo"
print (var[2:])                 # prints string starting from 3rd character: "llo World!"
print (var * 2)                 # prints string two times: "Hello World!Hello World!"
print (var + "TEST")            # prints concatenated string: "Hello World!TEST"

# Lists
biglist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]      # list with 5 values
tinylist = [123, 'john']                            # list with 2 values

print (biglist)                 # prints complete list: "['abcd', 786, 2.23, 'john', 70.200000000000003]"
print (biglist[0])              # prints first element of the list: "abcd"
print (biglist[1:3])            # prints elements starting from 2nd till 3rd: "[786, 2.23]"
print (biglist[2:])             # prints elements starting from 3rd element: "[2.23, 'john', 70.200000000000003]"
print (tinylist * 2)            # prints list two times: "[123, 'john', 123, 'john']"
print (biglist + tinylist)      # prints concatenated lists: "['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']"

# Tuples
bigtuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (bigtuple)                # prints complete tuple: "('abcd', 786, 2.23, 'john', 70.200000000000003)"
print (bigtuple[0])             # prints first element of the tuple: "abcd"
print (bigtuple[1:3])           # prints elements starting from 2nd till 3rd: "(786, 2.23)"
print (bigtuple[2:])            # prints elements starting from 3rd element: "(2.23, 'john', 70.200000000000003)"
print (tinytuple * 2)           # prints tuple two times: "(123, 'john', 123, 'john')"
print (bigtuple + tinytuple)    # prints concatenated tuple: "('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')"

# ---------------------- ERROR -------------------------

# tuples cannot be updated. trying to update a tuple will give an error
bigtuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
biglist = [ 'abcd', 786 , 2.23, 'john', 70.2  ]

bigtuple[2] = 1000               # invalid syntax with tuple
biglist[2] = 1000                # valid syntax with list

# --------------------------------------------------------

# Dictionaries
sampledict = {}
sampledict['one'] = "This is one"
sampledict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (sampledict['one'])       # prints value for 'one' key: "This is one"
print (sampledict[2])           # prints value for 2 key: "This is two"
print (tinydict)                # prints complete dictionary: "{'name': 'john', 'dept': 'sales', 'code': 6734}"
print (tinydict.keys())         # prints all the keys: "dict_keys(['name', 'dept', 'code'])"
print (tinydict.values())       # prints all the values: "dict_values(['john', 'sales', 6734])"

# Data type conversion functions

int()                           # converts value to an integer
float()                         # converts value to a floating point (decimal)
complex()                       # creates a complex number from values
str()                           # converts value to a string
repr()	                        # converts value to expression string
eval()	                        # evaluates string value and returns an object
tuple()                         # converts value to a tuple
list()                          # converts value to a list
set()                           # converts value to a set
dict()	                        # converts value to a dictionary
frozenset()                     # converts value to a frozen set
chr()                           # converts value to a char
unichr()                        # converts value to unicode char	
ord()	                          # converts a single character value to its integer value.
hex()                           # converts value to hexadecimal string
oct()                           # converts value to octal string
