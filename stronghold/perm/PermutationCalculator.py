import math
import itertools

with open('rosalind_perm.txt', 'r') as file:
    n = int(file.read().strip())
lis = []
for i in range(n):
    lis.append(i + 1)

tot = math.factorial(n)

print(tot)
permutations = list(itertools.permutations(lis))
permutations = '\n'.join([' '.join(map(str, perm)) for perm in permutations])

print(permutations)
