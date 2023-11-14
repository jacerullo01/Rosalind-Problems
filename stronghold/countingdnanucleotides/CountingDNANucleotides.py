with open ('rosalind_dna.txt', 'r') as file:
    DNA = file.read()
def countnucleaotides(DNA):
    A, C, G, T = 0, 0, 0, 0
    for nucleotide in DNA:
        if nucleotide == 'A':
            A += 1
        elif nucleotide == 'C':
            C += 1
        elif nucleotide == 'G':
            G += 1
        else:
            T += 1
    return f'{A} {C} {G} {T}'

result = countnucleaotides(DNA)
print(result)
