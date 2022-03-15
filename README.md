# Actividad 3.3 | Programando un DFA

DFA's (Deterministic Finite Automatons) are computational tools that are useful for analyzing strings and verifying their membership to a regular language.

### Requirements:

In order to run this program, a python interpreter is needed (python3, preferably).

## How to use

To run:
`python main.py {file path}`

Example test.

Testing the following txt file:

```
b = 7

a = 32.4 *(-8.6 - b)/       6.1e-8

d = a ^ b

10.0

+0

// c=35*19 ^ 3.     Esto es un comentario

_a25 // error
```

` python main.py ./test.txt`

Outputs

```b ----> Variable
= ----> Asignación
7 ----> Entero
a ----> Variable
= ----> Asignación
32.4 ----> Real
* ----> Multiplicación
( ----> Paréntesis que cierra
-8.6 ----> Real
- ----> Resta
b ----> Variable
) ----> Paréntesis que abre
/ ----> División
6.1e-8 ----> Real
d ----> Variable
= ----> Asignación
a ----> Variable
^ ----> Potencia
b ----> Variable
10.0 ----> Real
+0 ----> Entero
// c=35*19 ^ 3.     Esto es un comentario ----> Comentario
_a25 ----> Error
// error  ----> Comentario
```
