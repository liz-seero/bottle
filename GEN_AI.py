import random

class Cat:
    def __init__(self, cat_type, color, personality):
        self.cat_type = cat_type
        self.color = color
        self.personality = personality

def generate_cats():
    cat_types = ["Siamese", "Persian", "Maine Coon", "Ragdoll", "Sphynx", "Bengal", "Scottish Fold", "British Shorthair", "Russian Blue", "Norwegian Forest", "Bombay", "Abyssinian", "Siberian", "Burmese", "Oriental", "Devon Rex", "Manx"]
    colors = ["black", "white", "orange", "grey"]
    personalities = ["happy", "sad"]

    cats = []
    for _ in range(len(cat_types)):
        cat_type = random.choice(cat_types)
        color = random.choice(colors)
        personality = random.choice(personalities)
        cats.append(Cat(cat_type, color, personality))
    return cats

def match_cats(cats):
    matched_cats = []
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            if cats[i].color == cats[j].color and cats[i].personality == cats[j].personality:
                matched_cats.append((cats[i], cats[j]))
    return matched_cats

def main():
    cats = generate_cats()
    matched_cats = match_cats(cats)

    print("Generated Cats:")
    for cat in cats:
        print(f"Type: {cat.cat_type}, Color: {cat.color}, Personality: {cat.personality}")

    print("\nMatched Cats:")
    for cat1, cat2 in matched_cats:
        print(f"Cat 1: Type-{cat1.cat_type}, Color-{cat1.color}, Personality-{cat1.personality}")
        print(f"Cat 2: Type-{cat2.cat_type}, Color-{cat2.color}, Personality-{cat2.personality}")
        print()

    print(f"Total matched pairs: {len(matched_cats)}")

if __name__ == "__main__":
    main()

import random

class Animal:
    def __init__(self, species, color, personality):
        self.species = species
        self.color = color
        self.personality = personality

def generate_animals(species, num_animals):
    colors = ["black", "white", "orange", "grey"]
    personalities = ["happy", "sad"]

    animals = []
    for _ in range(num_animals):
        color = random.choice(colors)
        personality = random.choice(personalities)
        animals.append(Animal(species, color, personality))
    return animals

def match_animals(animals):
    matched_animals = []
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            if animals[i].color == animals[j].color and animals[i].personality == animals[j].personality:
                matched_animals.append((animals[i], animals[j]))
    return matched_animals

def count_animals(animals, species):
    return len(animals)

def main():
    # Generate animals for each shelter
    cat_shelter = generate_animals("cat", 17)
    dog_shelter = generate_animals("dog", 20)
    parrot_shelter = generate_animals("parrot", 15)
    bird_shelter = generate_animals("bird", 12)
    elephant_shelter = generate_animals("elephant", 10)

    # Match animals for each shelter
    cat_matches = match_animals(cat_shelter)
    dog_matches = match_animals(dog_shelter)
    parrot_matches = match_animals(parrot_shelter)
    bird_matches = match_animals(bird_shelter)
    elephant_matches = match_animals(elephant_shelter)

    # Count animals in each shelter
    cat_count = count_animals(cat_shelter, "cat")
    dog_count = count_animals(dog_shelter, "dog")
    parrot_count = count_animals(parrot_shelter, "parrot")
    bird_count = count_animals(bird_shelter, "bird")
    elephant_count = count_animals(elephant_shelter, "elephant")

    # Print results
    print("Number of animals in each shelter:")
    print(f"Cat Shelter: {cat_count}")
    print(f"Dog Shelter: {dog_count}")
    print(f"Parrot Shelter: {parrot_count}")
    print(f"Bird Shelter: {bird_count}")
    print(f"Elephant Shelter: {elephant_count}")

if __name__ == "__main__":
    main()
