n = 87
m = 17
pop = [1, 1]
dead = []
for i in range(0, n):
    if i < m:
        dead.append(0)
    elif i == m:
        dead.append(-1)
    else:
        dead.append(dead[i-1] + dead[i-2] - 1)

for i in range(2, n):
    pop.append(pop[i-1] + pop[i-2])
for i in range(2, n):
    pop[i] += dead[i]

print(pop[n-1])