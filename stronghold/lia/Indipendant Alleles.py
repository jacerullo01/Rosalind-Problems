with open ('rosalind_iev.txt', 'r') as file:
    data = file.read().strip().split(' ')
k = data[0]
n = data[1]

start = 0
for i in k:
