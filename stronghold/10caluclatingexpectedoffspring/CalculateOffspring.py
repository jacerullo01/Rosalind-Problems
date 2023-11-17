with open ('rosalind_iev.txt', 'r') as file:
    data = file.read().strip().split(' ')
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
e = int(data[4])
f = int(data[5])

result = 2*a + 2*b + 2*c + 1.5*d + 1*e + 0*f
print(result)