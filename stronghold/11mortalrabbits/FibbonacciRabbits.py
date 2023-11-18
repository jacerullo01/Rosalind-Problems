n = 6
m = 3
pop = [1, 1]

for i in range(2, n):
    if i<m:
        pop.append(pop[i-1] + pop[i-2])
    else:
        pop.append(pop[i-1] + pop[i-2] - pop[i-m])

print(pop)