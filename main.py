from qm import QM

f = QM("ABC", [4, 5, 6, 7])
print(f.solve()) # --> A
 
g = QM("ABC", [3, 4, 5, 6, 7])
print(g.solve()) # --> A + B*C

# # # # #

f = QM("ABC", [0, 1, 2, 3], is_maxterm = True)
print(f.solve()) # --> A'
 
g = QM("ABC", [0, 1, 2], is_maxterm = True)
print(g.solve()) # --> (A'+B')*(A'+C')

# # # # #

f = QM("ABC", [0, 1], dont_cares = [4, 5, 6, 7])
print(f.solve()) # --> B'
 
g = QM("ABCD", [0, 2, 4, 8, 12], dont_cares = [6, 10, 11, 14, 15])
print(g.solve()) # --> D'