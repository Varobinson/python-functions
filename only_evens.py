def only_evens():
    num = [11, 20, 42, 97, 23, 10]
    even_num = []
    for nums in num:
        if nums % 2 == 0:
            even_num.append(nums)
    print(even_num)

only_evens()
