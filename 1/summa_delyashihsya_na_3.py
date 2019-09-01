a, b = (input().split())
a = int(a)
b = int(b)
c, d = 0, 0
for i in range(a, b+1):
    if i%3 == 0:
        c = c + i
        d = d + 1
        print(i, ' ', d)
print(c/d)