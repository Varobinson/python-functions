def temp(cel):
    return (cel * 9/5) + 32
try:
    user_cel = int(input('What is the temperature? '))
except ValueError:
    print('Must be a number')


fahrenheit = temp(user_cel)
print(fahrenheit)
