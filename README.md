# PyQM
A Python project for simplifying logical expressions using the Quine-McCluskey Algorithm

## How to Use
There are 2 different ways to get a simplified logical expression:
 * Minterm method
 * Maxterm method
 
Both methods will get you the same function but they differ by how they are connected together
 * `A' + B'` (Minterm method) is the exact same as `AB` (Maxterm method)

### Minterm Method

```py
f = QM("ABC", [4, 5, 6, 7])
print(f.solve()) # --> A

g = QM("ABC", [3, 4, 5, 6, 7])
print(g.solve()) # --> A + B*C
```

### Maxterm Method

```py
f = QM("ABC", [0, 1, 2, 3], is_maxterm = True)
print(f.solve()) # --> A'

g = QM("ABC", [0, 1, 2], is_maxterm = True)
print(g.solve()) # --> (A'+B')*(A'+C')
```

### Using Don't Cares

```py
f = QM("ABC", [0, 1], dont_cares = [4, 5, 6, 7])
print(f.solve()) # --> B'

g = QM("ABCD", [0, 2, 4, 8, 12], dont_cares = [6, 10, 11, 14, 15])
print(g.solve()) # --> D'
```

## Feedback, Suggestions, Bugs

Any feedback, suggestions, or bugs can be mentioned in my [Discord Server](https://discord.gg/EpjKcrm).
