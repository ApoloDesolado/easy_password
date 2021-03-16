# Easy Password
## Script to generate a secure and rememorable password.

When it comes to create a password for some of our accounts,
it becomes harder to remember a password as we increase its entropy.

The approach of this script is to make it easier to generate rememorable
passwords with a good amount of entropy.

## parameters:
* **phrase**: phrase to convert into a password.
* **password_lenght**: minimum lenght required for the password (the result might be longer).
* **alternatives**: number of alternative passwords to return (so the user chooses one).
----------------------

## functions:
+ easy_password.**is_possible**(phrase, password_lenght):  
   defines wether or not it is possible to generate a password.  

+ it will return two values:
   + **possible(bool)**: if it's possible
   + **why(str)**: if the given phrase is too long or too short, and how many
      characters/words should be added/removed

+ easy_password.**passwords**(phrase, password_lenght, alternatives):  
   + It will generate the number of required passwords and return them as a list.  

----------------------

## Usage example:

```python
from easy_password import is_possible, passwords
phrase = "Today is gonna be a nice day, I can feel it in the air!"
password_lenght = 12
alternatives = 5

possible, why = is_possible(phrase, password_lenght)
if possible:
    password_alternatives = passwords
    print(password_alternatives)
else:
    print(why)
```
