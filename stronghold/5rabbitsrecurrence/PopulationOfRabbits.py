# Original fibbonacci sequence is Fn = Fn-1 + Fn-2 where F1=F2=1
# Mine is Fn = Fn-1 + K(Fn-2) where F1=F2=1, where k and n are given
n = 12
k = 1
pop = [1,1] # index 0 is n=1, index 1 is n=2 and so on
for i in range(2, n):
    pop.append(pop[i-1] + k*[i-2])
print(pop)