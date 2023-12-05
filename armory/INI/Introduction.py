from Bio.Seq import Seq
with open('rosalind_ini.txt', 'r') as file:
    DNA = Seq(file.read())
print(f'{DNA.count("A")} {DNA.count("C")} {DNA.count("G")} {DNA.count("T")}')
