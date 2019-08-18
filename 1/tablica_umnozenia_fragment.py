a = int(input())
b = int(input())
c = int(input())
d = int(input())
#print('\t', end='')
for i in range(c, d+1):
     print('\t', i, end='')
print()
for j in range(a, b+1):
    print(j, '\t', end='')
    for i in range(c, d+1):
        print(j * i, '\t', end='')
    print()
