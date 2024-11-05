q = int(input())
while q:
    n = int(input())
    s = str(input())
    ans = ''
    i = 0
    j = 0
    for i in range(0, n - 3):
        j = i + 2

        if (s[j]) != '0':
            v = int(s[i])
            ans = ans + chr(96 + v)
        elif (s[j]) == '0':
            v = int(s[i:i + 2])
            ans = ans + chr(96 + v)
            i = i+3

    v = int(s[-2])
    ans = ans + chr(96 + v)

    v = int(s[-1])
    ans = ans + chr(96 + v)
    print(ans)
    q = q - 1


