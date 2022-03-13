
import random

if __name__ == '__main__':

    play = True

    while play:

        choices = ['rock', 'paper', 'scissors']

        usersScore = 0
        programsScore = 0

        for index in range(5):

            if index == 0:
                print('------------------------------------------------')
                print('Let\'s play rock, paper, scissors!')

            usersChoice = ''
            errorMessage = ''

            print('------------------------------------------------')
            print(f'ROUND {index + 1}')

            while usersChoice not in choices:
                if usersChoice != '':
                    errorMessage = 'Sorry, that is not an option. '
                usersChoice = input(f'{errorMessage}Please choose rock, paper or scissors: ').lower()

            usersChoice = choices.index(usersChoice)

            programsChoice = random.randint(0, 2)

            print(f'User chose: {choices[usersChoice]} | Program chose {choices[programsChoice]}')

            if usersChoice == programsChoice:
                print('It\'s a tie!')
            elif (usersChoice == 0 and programsChoice == 2) \
                    or (usersChoice == 1 and programsChoice == 0) \
                    or (usersChoice == 2 and programsChoice == 1):  # rock
                print(f'User wins round {index + 1}')
                usersScore += 1
            else:
                print(f'Program wins round {index + 1}')
                programsScore += 1

            print('------------------------------------------------')

            if index == 4:
                print('The final score is:')
            else:
                print('The current score:')

            print(f'User: {usersScore} | Program: {programsScore}')

            if index == 4:
                if usersScore > programsScore:
                    print('Congratulations! You win!')
                elif usersScore == programsScore:
                    print('It\'s a tie!')
                else:
                    print('You lose.')
                print('------------------------------------------------')

        playAgain = ''
        playAgainOptions = ['yes', 'no']

        while playAgain not in playAgainOptions:
            if playAgain != '':
                playAgainError = 'Please try again: '
            else:
                playAgainError = ''
            playAgain = input(f'{playAgainError}Would you like to play again? (yes / no) ').lower()

        if playAgain == 'yes':
            play = True
        else:
            play = False

    print('------------------------------------------------')
    print('Thanks for playing!')
