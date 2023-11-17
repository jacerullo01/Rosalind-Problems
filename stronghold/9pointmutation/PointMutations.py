with open ('rosalind_hamm.txt', 'r') as file:
    DNA = file.read().strip().split('\n')
DNA1 = list(DNA[0])
DNA2 = list(DNA[1])
mutations = 0
for nuc in range(len(DNA1)):
    if DNA1[nuc] != DNA2[nuc]:
        mutations += 1
print(mutations)