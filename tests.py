from easy_password import passwords, is_possible

def generate_passwords(phrase):
    possible, why = is_possible(phrase, lenght)
    if possible:
        possible_passwords=passwords(phrase, lenght, alternatives)
        print(phrase)
        print(possible_passwords)
    else:
        print(f"{why}, ({phrase})")

phrases=[
        "Hello, friend", "I would like to join your team, mate",
        "My grandpa says he got a new gun", "I tried to cry, but I couldn't",
        "I don't think you can join our team, mate", "how dare you!"
]

lenght=12        # Desired lenght for the generated passwords.
alternatives=5   # Number of alternative passwords to generate.

# Testing each phrase from the list.
for phrase in phrases:
    generate_passwords(phrase)
    print("-"*33)
