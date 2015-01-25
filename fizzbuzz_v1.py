## Version 1:
 
# Hard-coded upper limit:
n = 100
 
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