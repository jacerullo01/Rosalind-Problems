with open ('rosalind_cons1.txt', 'r') as file:
    dataset = file.read().strip().replace('\n', '')
dataset = dataset.split('>Rosalind_')
if dataset[0] == '':
    del dataset[0]
def count(DNA, nuc):
    count = 0
    for nucleotide in DNA:
        if nucleotide == nuc:
            count +=1
    return count
DNA = []
profile = []
for i in range(len(dataset)):
    DNA.append(list(dataset[i][1:]))
# [1:] could cause problems if the number is more than 1 digit
counter = [[row[i] for row in DNA] for i in range(len(DNA[0]))]
profile = {'A': [], 'C': [], 'G': [], 'T': []}
for i in counter:
    profile['A'].append(count(i, 'A'))
    profile['C'].append(count(i, 'C'))
    profile['G'].append(count(i, 'G'))
    profile['T'].append(count(i, 'T'))
consensus = ''
for counts in zip(profile['A'], profile['C'], profile['G'], profile['T']):
    max_count = max(counts)
    if max_count == counts[0]:
        consensus += 'A'
    elif max_count == counts[1]:
        consensus += 'C'
    elif max_count == counts[2]:
        consensus += 'G'
    else:
        consensus += 'T'


print(consensus)
for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")