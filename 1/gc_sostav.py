str = 'dftrggscgkgtvdc'
#str = input()
c = str.upper().count('C')
g = str.upper().count('G')
print(c, g, len(str), str)
print((c + g )/ len(str) * 100)
