s = 'ggttyuuuiikkkw'
ss = ''
i = 0
while i+1:
    i+=1
    print(s[i])
if s[-1] != s[-2]: # обрабатываем последний знак не равный предыдущему
    ss = ss + s[-1] + '1'
else:
    print(s)