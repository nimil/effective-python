names = ['John', 'Smith', 'Amma']
counts = [len(name) for name in names]
print(counts)

countMax = 0
nameMax = ''

for name,count in zip(names, counts):
    if count > countMax:
        countMax = count
        nameMax = name
print(nameMax,countMax)

#只要其中最短的函数走完了就不在往下遍历了 木桶效应
