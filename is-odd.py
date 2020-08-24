# Initiating function
def is_even(num):
    #finding remainder if even print true
    if num % 2 == 0:
        return True
    else:  # if odd print false
        return False


def is_odd(num):
    if not is_even(num):
        print('odd')
    else:
        print('even')


#handling value errors
try:
    user_input = int(input('Enter a number! '))
except ValueError:
    print('Must input a number')

is_odd(user_input)


