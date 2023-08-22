
import random
from math import *


#lists of animals types

water = [
    "Crab", "Fish", "Seal", "Shark", "Starfish", "Whale", "Penguin",
"Jellyfish", "Lobster", "Pelican", "Seahorse", "Walrus", "Shrimp",
"Oyster", "Clams", "Seagull", "Dolphin", "Cormorant", "Otter", "Angelfish",
"Blue Whale", "Tuna", "Salmon", "Goldfish", "Barnacle", "Bull Shark",
"Clownfish", "Cod", "Conch", "Coral", "Cuttlefish", "Dolphin", "Fan Worm",
"Flounder", "Flying Fish", "Grouper", "Haddock", "Halibut", "Herring",
"Humpback Whale", "Jellyfish", "Ling", "Lobster", "Mackerel", "Mussel"
]

wild = [
    "Tiger", "Lion", "Elephant", "Leopard", "Panther", "Cheetah", "Wolf",
"Hyena", "Giraffe", "Deer", "Zebra", "Gorilla", "Monkey", "Bear",
"Squirrel", "Kangaroo", "Crocodile", "Panda", "Squirrel", "Mongoose",
"Koala Bear", "Wombat", "Meerkat", "Otter", "Hedgehog", "Raccoon", "Hare",
"Mole", "Rabbit", "Alligator", "Oryx", "Elk", "Badger", "Pangolin",
"Camel", "Coyote", "Bison", "African Elephant", "Antelope", "Alpine Goat",
"Beaver", "Baboon", "Bat", "Giant Panda", "Chihuahua", "Orangutan"
]

sky = [
    "Eagle", "Hawk", "Emu", "Falcon", "Owl", "Bat", "Chihuahua", "Guinea Pig"
]

#----------------------------------------
# Randomly choose an animal from each category

animals = [random.choice(water) , random.choice(wild) , random.choice(sky)]
picked_animal=random.choice(animals)
print("")


# Check if a string contains spaces

def spaces(x):
    for i in x:
        if i == " ":
            return True
    return False


# Check if the picked animal's name contains spaces

if spaces(picked_animal)==True:
    print ("this name has an *SPACE*")





print(picked_animal)
print("")

# Determine the category of the picked animal

if picked_animal in sky:
    print("animal is from the sky")
    
elif picked_animal in wild:
    print("animal is from the wild")

else:
    print("animal is from the water")

# Initialize the guessed animal with hidden characters

guessed_animal = picked_animal[0] + '*' * (len(picked_animal) - 1)
print("The animals start with the letter", guessed_animal)
print("")
attempts=0
for i in range(3): # Allow three attempts
    attempts += 1
    user_guess = input("Enter your guess: ").capitalize()  
    if user_guess == picked_animal:
        print("Congratulations! You guessed correctly.")
        break
    else:
        # Reveal one more character if the guess is incorrect
        revealed_chars = min((i+1) + 1, len(picked_animal)-1)
        guessed_animal = picked_animal[:revealed_chars] + '*' * (len(picked_animal) - revealed_chars)
        while attempts<3:
            print("Incorrect guess. The animals start with the letters", guessed_animal)
            break

print("")
print("The correct animal was:", picked_animal)