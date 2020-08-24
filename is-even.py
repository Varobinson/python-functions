# Initiating function
def is_even(num):
    #finding remainder if even print true
    if num % 2 == 0:
        return True
    else:  # if odd print false
        return False
#handling value errors
try:
    user_input = int(input('Enter a number! '))
except ValueError:
    print('Must input a number')
   
answer = is_even(user_input)
print(answer)
