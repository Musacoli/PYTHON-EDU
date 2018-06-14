"""Mad Libs have short stories that a player can
fill in. The result is usuall funny (or strange)
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print ('Mad Libs has started')

name = input('Enter a name: ')
adj1 = input('Enter 1st adjective: ')
adj2 = input('Enter 2nd adjective: ')
adj3 = input('Enter 3rd adjective: ')

verb = input('Enter a verb: ')

noun1 = input('Enter a noun: ')
noun2 = input('Enter another noun: ')

animal = input('Enter an animal name: ')
food = input('Enter your favourite snack: ')
fruit = input('Enter your favourite fruit: ')
superh = input('Enter your best superhero: ')
country = input('Enter your country: ')
dessert = input('Enter your best dessert: ')
year = input('Enter any future year: ')

while true:
    print (STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superh, name, country, name, dessert, name, year, noun2))
