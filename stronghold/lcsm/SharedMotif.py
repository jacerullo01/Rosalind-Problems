with open ('rosalind_lcsm1.txt', 'r') as file:
    dataset = file.read().strip().replace('\n', '')
dataset = dataset.split('>Rosalind_')
if dataset[0] == '':
    del dataset[0]
DNA = []
for i in range(len(dataset)):
    DNA.append((dataset[i][1:]))
print(DNA)
