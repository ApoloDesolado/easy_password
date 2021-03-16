# Easy Password
## Script para generar una contraseña larga, segura y fácil de recordar.

Cuando se trata de crear una contraseña para alguna cuenta, recordar
la contraseña se vuelve más difícil conforme aumentamos su entropía.

El enfoque de este script es hacer fácil la creación de contraseñas
recordables con una buena cantidad de entropía.

## Parámetros:
* **phrase**: frase para convertir en contraseña.
* **password_lenght**: largo mínimo del que se requiera la contraseña (el resultado puede ser más largo).
* **alternatives**: numero de contraseñas alternativas generadas (para que el usuario elija una).
----------------------

## Funciones:
+ easy_password.**is_possible**(phrase, password_lenght):  
   Define si es posible o no generar una contraseña con los parámetros dados.  

  **Valores obtenidos**:
   + **possible (bool)**: si es posible o no.
   + **why (str)**: en caso de que **possible** sea False, **why** es la razón por qué no es posible (si la frase es muy corta o muy larga).

+ easy_password.**passwords**(phrase, password_lenght, alternatives):  
   + Generará el número requerido de contraseñas.  
   
  **Valores obtenidos**:  
   + **passwords (list)**: Alternativas de contraseñas.

----------------------

## Ejemplo de uso:

```python
from easy_password import is_possible, passwords
phrase = "Ahora podré recordar todas mis contraseñas!"
password_lenght = 12
alternatives = 5

possible, why = is_possible(phrase, password_lenght)
if possible:
    password_alternatives = passwords
    print(password_alternatives)
else:
    print(why)
```
