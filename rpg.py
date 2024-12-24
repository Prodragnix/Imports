import random
option=['Rock','Paper','Scissors']
user=input('Choose between rock , paper and scissors:\n')
computer=random.choice(option)
if user==computer:
    print('We both got the same!')
elif user=='Rock' and computer =='Scissors':
    print('Rock smashes scissors!You win!')
elif user=='Paper' and computer =='Rock':
    print('Paper covers rock!You win!')
elif user=='Scissors' and computer =='Paper':
    print('Scissors cuts paper!You win!')
else:
    print('You lose!Better luck next time! I got:',computer)