with open ('rosalind_revp1.txt', 'r') as file:
    dataset = file.read().split('\n')
del dataset[0]
DNA = list(dataset[0])
def reverse(sc):
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
    return list((''.join(sc)))
def getIndexes(s, t):
    indexes = []
    for i in range(len(s) - len(t)+1):
        if s[i:i+len(t)] == t:
            indexes.append(str(i+1))

    return(indexes)

print(DNA)
print(reverse(DNA))