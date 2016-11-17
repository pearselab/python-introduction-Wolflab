from __future__ import print_function
import math
#1. Write a loop that prints out the numbers from 20 to 10

for i in range(20,9, -1):
    print(i)
   
# 2. Now with list comprehension
x = [print(i) for i in range(20,9,-1)]


#3. Write a loop that prints out only the numbers from 20 to 10 that are even

even_list = []
for i in range(20,9, -1):
    if i%2 == 0:
        even_list.append(i)
print(even_list)


#4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even
x = [print(i) for i in range(20,9,-1) if i%2 == 0]

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
 
# Let us  test            
x = 199
if is_prime(x):
    print( x, "is prime")
else:
    print(x, "is not prime")
    
# 6. Write a function that loads a text file, loops over the lines in it, and prints out the
# fifth character on the fifth line of that file.
# Sorry - I know this is ugly
with open("test_text.txt") as data:
    line_counter = 1
    for line in data:
        if line_counter == 5:
            print(line[4])
        line_counter+=1
        
        
# Ok Wolf, you moron. You can do this as list comprehension
with open("test_text.txt") as data:
    x = [print(line[4])for line in data if line == 4]

# 7. Write a loop that prints out the numbers from 1 to 20, printing “Good: NUMBER” if the number is
# divisible by five and “Job: NUMBER” if then number is prime, and nothing otherwise.

def is_div_by_five(x):
    return True if x%5 == 0 else False

for i in range(1,20):
    if i == 5:
        print("good job ", i)
    elif is_div_by_five(i):
        print("good ", i)
    elif is_prime(i):
        print("job ", i)


# 8. A biologist is modelling population growth using a Gompertz curve, which is defined as y(t) = a.e−b.e−c.t
# where y is population size, t is time, a and b are parameters, and e is the exponential function. Write
# them a function that calculates population size at any time for any values of its parameters.

def gompertz(a, b, c, t):
    return(a * math.exp(-b * math.exp(-c * t)))

print(gompertz(2, 3, 4, 5))


#9. Write a function that draws boxes of a specified width and height that look like this (height 3, width 5):
#*****
#* *
#*****
#(Hint: what does print("*" + "" + "*"*4) give you?)
# NOte the funky numbers are to get it to look pretty with command line run

def make_box(height, width):
    print(width * "*") # top line
    for row in range(height - 2): # middle bit
        print("*", " " * (width-4), "*")
    print(width * "*") # bottom line
make_box(17,19)
    