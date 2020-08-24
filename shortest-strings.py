def shortest(num):
    num.sort(key=len)
    print(num[0])


num = ['word','longest', 'huh', 'is']
shortest(num)
