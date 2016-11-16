from __future__ import print_function
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

def is_prime(numb):
    for i in range(numb-1,2,-1):
        if numb % i == 0:
            answer = False
            break
        else:
            answer = True
    return answer
 
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