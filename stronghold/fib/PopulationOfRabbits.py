n = 87
k = 17
pop = [1,1]
for i in range(2, n):
    pop.append(pop[i-1] + k * pop[i-2])
print(pop)