with open ('rosalind_revc.txt', 'r') as file:
    s = file.read()
sc = list(s[::-1])
scSize = len(sc)
A, C, G, T = [], [], [], []
for nuc in range(scSize):
    if sc[nuc] == 'A':
        A.append(nuc)
    elif sc[nuc] == 'C':
        C.append(nuc)
    elif sc[nuc] == 'G':
        G.append(nuc)
    elif sc[nuc] == 'T':
        T.append(nuc)
for nuc in range(scSize):
    if nuc in A:
        sc[nuc] = 'T'
    elif nuc in T:
        sc[nuc] = 'A'
    elif nuc in C:
        sc[nuc] = 'G'
    elif nuc in G:
        sc[nuc] = 'C'
print(''.join(sc))
