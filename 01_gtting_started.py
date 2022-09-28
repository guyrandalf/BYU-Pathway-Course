favColor = input('What is your favorite color? ')
# responseMsg = f'Your favorite color is {favColor}'
nickName = input('Give us your nickname? ')
ageValue = input('How old are you? ')
confirmChoice = input(f'Final answer, your favorite color is {favColor}? ')
responseMsg = f'Ah! {nickName}, you are {ageValue} years old and your favorite color is {favColor}! :) '
if confirmChoice.upper() == 'NO':
    print('You are not sure of your choice, please start over')
else:
    print(responseMsg)
