import random
#guessing number game

print('Welcome to the Guess game!!!')
print()

won = []

def again():
    while True:

        ran = [1,2,3,4,5]

        Random = random.choice(ran)
        
        guess = int(input('Guess a number between 1 and 5 '))

        if guess == Random:
            print()
            print('Congrats!!! You have got 1 points!!')
            print()
            won.append(1)
            total = sum(won)
            print(f'You have {total} in total')
            print()
            if total == 10:
                print('You have won this game!!!')
                print()
                break
        else:
            print()
            print('Your guess is not correct!!!')
            print()
            print('The guess number is',Random)
            print()
            print('Your point is reduced by 1')
            print()
            won.append(-1)
            total = sum(won)
            print(f'You have {total} in total')
            print()
            if total < 0:
                print('Unfortunately, you have failed this game!!!')
                print()
                again = input('Would you like to try again? ')
                if again.lower() == 'yes':
                    pass
                else:
                    print('Better luck next time')
                    break

again()
