# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.
import random

#create list of 100 random numbers from 0 to 1000
rand_list = [random.randint(0, 1000) for i in range(100)]

#sorting using bubble sort
for i in range(len(rand_list)):
    for j in range(len(rand_list) - 1):
        if rand_list[j] > rand_list[j + 1]:
            rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]

#creating lists for even and odd numbers
even_list = [even for even in rand_list if even % 2 == 0]
odd_list = [odd for odd in rand_list if odd % 2 != 0]

#counting average for even and printing to console
#using error handling in case of even list is empty
try:
    even_average = sum(even_list) / len(even_list)
    print(f'Even numbers list average: {even_average}')
except ZeroDivisionError:
    print("Even list is empty")
    
#counting average for odd and printing to console
#using error handling in case of even list is empty
try:
    odd_average = sum(odd_list) / len(odd_list)
    print(f'Odd number list average: {odd_average}')
except ZeroDivisionError:
    print("Odd list is empty")
