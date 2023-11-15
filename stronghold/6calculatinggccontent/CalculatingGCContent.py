dataset = '''>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
'''
dataset = dataset.split('\n')
print(dataset)
def getDNA(dataset):
    DNAList = []
    for DNA in range(len(dataset)):
        if DNA%2 == 1:
            DNAList+=dataset[DNA]

    return DNAList

print(getDNA(dataset))

DNA1 = list(dataset[1])
DNA2 = list(dataset[3])
DNA3 = list(dataset[5])
def getCG(DNA):
    CG = 0
    for nuc in range(len(DNA)):
        if DNA[nuc] == 'C' or DNA[nuc] == 'G':
            CG += 1
    result = CG/len(DNA)
    return result
print(DNA1)
print(getCG(DNA1))

