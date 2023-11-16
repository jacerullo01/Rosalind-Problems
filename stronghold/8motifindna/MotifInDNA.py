with open ('test.txt', 'r') as file:
    lines = file.read().strip().split('\n')
s = lines[0]
t = lines[1]
def getIndexes(s, t):
    indexes = []
    for i in range(len(s) - len(t)+1):
        if s[i:i+len(t)] == t:
            indexes.append(str(i+1))

    return(indexes)
print(' '.join((getIndexes(s, t))))

