with open ('.txt', 'r') as file:
    s = file.read()
s = 'AAAACCCGGT'
sc = s[::-1]
# need to switch a's and c's, t's and g's, already made it backwards
print(sc)