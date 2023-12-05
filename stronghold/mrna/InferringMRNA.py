with open('rosalind_mrna.txt', 'r') as file:
    proteins = list(file.read().strip())

counts = {
    'F': 2,
    'L': 6,
    'I': 3,
    'M': 1,
    'V': 4,
    'S': 6,
    'P': 4,
    'T': 4,
    'A': 4,
    'Y': 2,
    'Stop': 3,
    'H': 2,
    'Q': 2,
    'N': 2,
    'K': 2,
    'D': 2,
    'E': 2,
    'C': 2,
    'W': 1,
    'R': 6,
    'G': 4
}

tot = 1
for prot in proteins:
    tot = (tot * counts[prot]) % 1000000

tot = (tot * counts['Stop']) % 1000000

print(tot)
