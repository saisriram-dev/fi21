import random

low = 1
high = 100
options = ('Rock', 'Paper', 'Scissors')
cards1 = [str(i) for i in range(2, 11)]
ace_cards = "J,Q,K,A"
cards2 = ace_cards.split(",")
cards = cards1.extend(cards2) # It extends cards1 list with the ace cards and the cards list becomes none
print(cards1)

# To generate a random integer
num = random.randint(low, high) # Both the endpoints are inclusive
print(num)

# To generate a random floating point number between 0 and 1
number = random.random()
print(number)

# To get a random value from a built-in data structure
option = random.choice(options)
print(option)

# To randomize the order in a list
random.shuffle(cards1)
print(cards1)
