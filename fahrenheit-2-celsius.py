def temp(fah):
    return (fah - 32) * 5/9


try:
    user_cel = int(input('What is the temperature? '))
except ValueError:
    print('Must be a number')


celsius = temp(user_cel)
print(celsius)
