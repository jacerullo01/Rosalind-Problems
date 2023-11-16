with open ('rosalind_gc.txt', 'r') as file:
    dataset = file.read().strip().replace('\n', '')
dataset = dataset.split('>Rosalind_')
if dataset[0] == '':
    del dataset[0]
print(dataset)
DNA = {}
for element in dataset:
    key = element[:4]
    DNA[key] = list(element[4:])

print(DNA)
def getCG(DNA):
    CG = 0
    for nuc in range(len(DNA)):
        if DNA[nuc] == 'C' or DNA[nuc] == 'G':
            CG += 1
    result = CG/len(DNA)
    return result*100

for i in DNA:
    print(f'Rosalind_{i}\n{getCG(DNA[i])}')
