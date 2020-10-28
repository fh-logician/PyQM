from qm import QM

f = QM("ABC", [4, 5, 6, 7])
print(f.solve()) # --> A
 
g = QM("ABC", [3, 4, 5, 6, 7])
print(g.solve()) # --> A OR B AND C

# # # # # 

f = QM("ABC", [0, 1, 2, 3], is_maxterm = True)
print(f.solve()) # --> NOT A

g = QM("ABC", [0, 1, 2], is_maxterm = True)
print(g.solve()) # --> (NOT A OR NOT B) AND (NOT A OR NOT C)

# # # # #

f = QM("ABC", [0, 1], dont_cares = [4, 5, 6, 7])
print(f.solve()) # --> NOT B

g = QM("ABCD", [0, 2, 4, 8, 12], dont_cares = [6, 10, 11, 14, 15])
print(g.solve()) # --> NOT D