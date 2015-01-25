## Fizzbuzz Version 3.0
## Handling non-integer user input

# import sys module to allow user input at command line
import sys

## Handle situation if user has not supplied value at command line
try:
 	# handle error if user has not supplied value at command line:		
 	n = int(sys.argv[1]) # if value supplied at command line. use 'int' to convert input to integer
except IndexError:
	try:
		n = int(raw_input("Please enter a number up to 100: ")) # if user not supplied at initial load time
	except ValueError:
		n = int(raw_input("Please enter a numeric input up to 100: ")) # if user enters text at prompt
except ValueError: # if value supplied at command line is non-numeric
 	n = int(raw_input("Please enter a numeric input up to 100: "))

 # Print "Fizz buzz counting up to n"
print("Fizz buzz counting up to {}".format(n))
 
# Print each number on a new line. Replace divisible by 3 with 'Fizz'. Replace divisible by 5 with 'Buzz'
# Replace divisible by both 3 and 5 with 'FizzBuzz'
for n in range(1,(n+1)):
 if n % 3 == 0 and n % 5 == 0:
	print "Fizz Buzz"
 elif n % 3 == 0:
	print "Fizz"
 elif n % 5 == 0:
	print "Buzz"
 else:
	print n


# can you use a while loop in the exception handling? what if user keeps entering dud data

# TODO: test for n being <= 100