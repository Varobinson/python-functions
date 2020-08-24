def longest(num):
    num.sort(key=len)
    print(num[-1])


num = ['word', 'longest', 'huh', 'is']
longest(num)
