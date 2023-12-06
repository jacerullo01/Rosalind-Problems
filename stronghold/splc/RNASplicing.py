with open ('rosalind_splc.txt', 'r') as file:
    dataset = file.read().strip().replace('\n', '')
dataset = dataset.split('>Rosalind_')
if dataset[0] == '':
    del dataset[0]
tot = []
profile = []
for i in range(len(dataset)):
    tot.append(dataset[i][4:])
full = tot[0]
RNA = full
del tot[0]
intron = tot
for i in intron:
    RNA = RNA.replace(i, '')
RNA = RNA.replace('T','U')
rna = [RNA[i:i+3]for i in range(0, len(RNA), 3)]

protein = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'Stop',
    'UGG': 'W',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}
def getProtein(rna):
    proteins = []
    for nuc in rna:
        if protein.get(nuc) != 'Stop':
            proteins.append(protein.get(nuc))
        else:
            break
    return ''.join(proteins)

print(getProtein(rna))
