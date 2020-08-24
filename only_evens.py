num = [11, 20, 42, 97, 23, 10]

def only_evens(num):
    even_num = []
    for nums in num:
        if nums % 2 == 0:
            even_num.append(nums)
    return even_num

print(only_evens(num))
