k = 21
m = 19
n = 23

sum = k+m+n
a = (k/sum)*((k-1)/(sum-1)) # 100
b = (k/sum)*(m/(sum-1)) # 100
c = (k/sum)*(n/(sum-1)) # 100

d = (m/sum)*(k/(sum-1)) # 100
e = (m/sum)*((m-1)/(sum-1)) # 75
f = (m/sum)*(n/(sum-1)) # 50

g = (n/sum)*(k/(sum-1)) # 100
h = (n/sum)*(m/(sum-1)) # 50
i = (n/sum)*((n-1)/(sum-1)) # 0

prob = 1*a + 1*b + 1*c + 1*d + 0.75*e + 0.5*f + 1*g + 0.5*h + 0*i
print(prob)
