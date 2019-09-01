s = 'gtyyykkkffgfddd'
ss = ''
i = 0
if len(s) == 1: #если длина = 1 просто печатаем
    s = s + '1'
    print(s, end='')
else:
    d = s[0]
    i = 0
    while i < (len(s) - 1):
        c = 1
        while s[i] == s[i+1]:
            c = c + 1
            i = i + 1
        d = s[i] + str(c)
        ss = ss + d
        i = i + 1
    if s[-1] != s[-2]: # обрабатываем последний знак не равный предыдущему
        ss = ss + s[-1] + '1'
    else:
        ss = ss + s[-1]

    print(ss)
