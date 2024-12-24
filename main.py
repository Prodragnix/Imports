import random
print('GUESS THE NUMBER!!! It is between 1 and 10!')
playing=True
num= int(random.randint(1,10))
while playing:
    user=int(input('Enter your guess: '))
    if user == num:
        print('YOU WON! The number was: ',num)
        break
    else:
        print('Try again!')