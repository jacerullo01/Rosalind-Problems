with open ('rosalind_fibd.txt', 'r') as file:
    data = file.read().strip().split(' ')
n = int(data[0])
m = int(data[1])
pop = [1, 1]
for i in range(2, n):
    x = pop[i-1] + pop[i-2]
    if i == m:
        x-=1
    elif i > m:
        x -= pop[i - m - 1]

    pop.append(x)

print(pop[n-1])