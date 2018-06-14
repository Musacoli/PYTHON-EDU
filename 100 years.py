#This program is to be used to calculate the year at  which someone is to become 100 years"""

#This line asks for the user's name.

from datetime import datetime

now = datetime.now()

now = int(now.year)

print ( 'Year to make 100 has started:')


age = input('What is your age: ')
if age is not (float, int):
    print ('Wrong input, enter a figure only')
    continue
    
name = input('What is your name: ')

dob = (now-int(age))

year_of_100 = (dob + 100)

story =  'Hi  %s, You will be making 100 years in the year %s' 

print (story % (name, year_of_100))

print ('Program has ended')
