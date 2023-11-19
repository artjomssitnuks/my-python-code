import random

def generate_random_number():
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    print("Random number:", random_number)

if __name__ == "__main__":
    main()

print('Goodbye')
