# Easy Password
## Script to generate a secure and memorable passwords.

When it comes to create a password for some of our accounts,
it becomes harder to remember it as we increase its entropy.

The approach of this script is to make it easier to generate memorable
passwords with a good amount of entropy.

## Parameters:
* **phrase**: phrase to convert into a password.
* **password_lenght**: minimum lenght required for the password (the result might be longer).
* **alternatives**: number of alternative passwords to return (so the user chooses one).

----------------------

## Functions:
+ easy_password.**is_possible**(phrase, password_lenght):  
   Defines wether or not it is possible to generate a password with the given parameters.  

  **Return values**:
   + **possible (bool)**: wether it's possible or not.
   + **why (str)**: if the given phrase is too long or too short, and how many
      characters/words should be added/removed.

+ easy_password.**passwords**(phrase, password_lenght, alternatives):  
   Generates the required amount of passwords.  
  **Return values**:
   + **passwords (list)**: Alternative passwords. 

----------------------

## Usage example:

```python
from easy_password import is_possible, passwords
phrase = "Today is gonna be a nice day, I can feel it in the air!"
password_lenght = 15
alternatives = 5

possible, why = is_possible(phrase, password_lenght)
if possible:
    password_alternatives = passwords(phrase, password_lenght, alternatives)
    print(f"Generated passwords from '{phrase}':")
    for idx, passwd in enumerate(password_alternatives):
        print(f"{idx+1}.- {passwd}")
else:
    print(why)
```
## Output:
   Generated passwords from 'Today is gonna be a nice day, I can feel it in the air!':  
   1.- 74¡96anD1(F¡17a  
   2.- 7I96aNcd1(fI1T@  
   3.- Td1Gb@Nd1cF1¡Ta  
   4.- tI&b@ND1(f3I¡t4  
   5.- 7aiG6aND¡(fiIT@  
