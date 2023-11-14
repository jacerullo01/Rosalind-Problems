# with open ('.txt', 'r') as file:
#    s = file.read()
s = 'AAAACCCGGT'
sc = list(s[::-1])
scSize = len(sc)
# need to switch a's and c's, t's and g's, already made it backwards
print(sc)
A = []
C = []
G = []
T = []
for nuc in range(scSize):
    if sc[nuc] == 'A':
        A.append(nuc)
    elif sc[nuc] == 'C':
        C.append(nuc)
    elif sc[nuc] == 'G':
        G.append(nuc)
    else:
        T.append(nuc)

for nuc in range(scSize)
print(A)
print(C)
print(G)
print(T)
