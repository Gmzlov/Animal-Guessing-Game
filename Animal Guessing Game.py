
import random


#lists of animals types

water = [
    "Crab", "Fish", "Seal", "Octopus", "Shark", "Starfish", "Whale", "Penguin",
    "Jellyfish", "Squid", "Lobster", "Pelican", "Seahorse", "Walrus", "Shrimp",
    "Oyster", "Clams", "Seagull", "Dolphin", "Shells", "Sea urchin", "Cormorant",
    "Otter", "Pelican", "Sea anemone", "Sea turtle", "Sea lion", "Coral",
    "Water Turtle", "Crocodile", "Killer Whale", "Sea Lion", "Sea Anemone",
    "Angelfish", "Blue Whale", "Piranha", "Platypus", "Tuna", "Eal", "Salmon",
    "Goldfish", "Abalone", "Albacore", "Anchovy", "Angelfish", "Barnacle",
    "Barracuda", "Blue Crab", "Blue Whale", "Bull Shark", "Cleaner wrasse",
    "Clownfish", "Cod", "Conch", "Coral", "Crown of Thorns", "Cuttlefish",
    "Dolphin", "Dottyback", "Dragonet", "Driftfish", "Dugong or Sea Cow",
    "Dungeness Crab", "Eel", "Elephant Seal", "Emperor Shrimp",
    "Estuarine Crocodile", "Fan Worm", "Flounder", "Flying Fish", "Fugu",
    "Giant Squid", "Great White Shark", "Grouper", "Grunion", "Haddock",
    "Hake", "Halibut", "Herring", "Humpback Whale", "Irukandji", "Isopods",
    "Jellyfish", "John Dory", "Killer Whale or Orca", "King Mackerel or Kingfish",
    "Krill", "Lamprey", "Leafy Sea Dragon", "Ling", "Lionfish", "Lobster",
    "Mackerel", "Mahi-mahi or Dorado", "Manatee or Sea Cow", "Manta Ray",
    "Megalodon", "Mulloway", "Mussel", "Narwhal"
]

wild = [
    "Tiger", "Lion", "Elephant", "Leopard", "Panther", "Cheetah", "Wolf", "Jaguar",
    "Hyena", "Giraffe", "Deer", "Zebra", "Gorilla", "Monkey", "Chimpanzee", "Bear",
    "Wild Boar", "Hippopotamus", "Kangaroo", "Rhinoceros", "Crocodile", "Panda",
    "Squirrel", "Mongoose", "Porcupine", "Koala Bear", "Wombat", "Meerkat", "Otter",
    "Hedgehog", "Possum", "Chipmunk", "Squirrel", "Raccoon", "Jackal", "Hare", "Mole",
    "Rabbit", "Alligator", "Monitor Lizard", "Oryx", "Elk", "Badger", "Dinosaur",
    "Pangolin", "Mole", "Okapi", "Camel", "Wild cat", "Coyote", "Bison", "African Elephant",
    "Aardvark", "Antelope", "Alpine Goat", "Komodo Dragon", "Bearded Dragon",
    "Royal Bengal Tiger", "Flying Squirrel", "Emu", "Eagle", "Eel", "Asiatic Lion",
    "Armadillo", "Beaver", "Emperor Penguin", "Baboon", "Bat", "Chameleon", "Bull",
    "Giant Panda", "Chihuahua", "Orangutan", "Chinchillas", "Hawk", "Iguana", "Ibis",
    "Ibex", "King Cobra", "Jellyfish", "Goose", "Walrus", "Seal", "Skink", "Markhor",
    "Falcon", "Bull Shark", "Arctic Wolf", "Owl", "Bulbul", "Bobcat", "Guinea Pig",
    "Yak", "Reindeer", "Moose", "Puma", "Okapi", "Marten", "Squirrel Monkey", "Caracal"
]

sky = [
    "Eagle", "Hawk", "Bulbul", "Emu", "Flying Squirrel", "Ibis", "Falcon", "Owl",
    "Bat", "Chihuahua", "Guinea Pig"
]

#----------------------------------------
animals = [random.choice(water), random.choice(wild), random.choice(sky)]


# Initialize the guessed animal with hidden characters
guessed_animal = animals[0][0] + '*' * (len(animals[0]) - 1)
print("The animals start with the letter", guessed_animal)

for i in range(3):  # Allow three attempts
    user_guess = input("Enter your guess: ").capitalize()

    if user_guess == animals[0]:
        print("Congratulations! You guessed correctly.")
        break
    else:
        # Reveal one more character if the guess is incorrect
        revealed_chars = min((i + 1) + 1, len(animals[0]) - 1)
        guessed_animal = animals[0][:revealed_chars] + '*' * (len(animals[0]) - revealed_chars)
        print("Incorrect guess. The animals start with the letter", guessed_animal)
print("")
print("The correct animal was:", animals[0])