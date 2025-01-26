import random
import string

# Step 1: Define the lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Funny", "Mighty", "Wild", "Silly", "Brave", "Loyal"]
nouns = ["Tiger", "Dragon", "Panda", "Shark", "Eagle", "Unicorn", "Lion", "Wolf"]

# Step 2: Generate a random username
def generate_username(include_numbers=False, include_special_chars=False, username_length=10):
    # Combine random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Add numbers or special characters if requested
    username = adjective + noun
    
    # Optionally add numbers
    if include_numbers:
        username += str(random.randint(0, 999))
    
    # Optionally add special characters
    if include_special_chars:
        special_chars = random.choice(string.punctuation)
        username += special_chars
    
    # Ensure the username length does not exceed the specified length
    if len(username) > username_length:
        username = username[:username_length]
    
    return username

# Step 3: Save the generated usernames to a text file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")

# Step 4: Interactive User Input
def get_user_input():
    print("Welcome to the Random Username Generator!")
    include_numbers = input("Include numbers in the username? (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters in the username? (yes/no): ").lower() == "yes"
    username_length = int(input("Enter the maximum length of the username: "))
    
    return include_numbers, include_special_chars, username_length

def main():
    # Get user input
    include_numbers, include_special_chars, username_length = get_user_input()
    
    # Generate a list of usernames
    generated_usernames = [generate_username(include_numbers, include_special_chars, username_length) for _ in range(10)]
    
    # Show the generated usernames
    print("\nGenerated Usernames:")
    for username in generated_usernames:
        print(username)
    
    # Save the usernames to a file
    save_usernames_to_file(generated_usernames)
    print("\nUsernames have been saved to 'usernames.txt'.")

# Run the program
if __name__ == "__main__":
    main()
