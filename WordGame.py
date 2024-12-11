import os

secretWord = 'newjeans'
correctLetters = ''
tryTimes = 0
level = 1

while True:
    typedLetter = input('Type a letter: ')
    tryTimes += 1

    if len(typedLetter) > 1:
        print('Type just one letter.')
        continue

    if typedLetter in secretWord:
        correctLetters += typedLetter

    showWord = ''
    for secretLetter in secretWord:
        if secretLetter in correctLetters:
            showWord += secretLetter
        else:
            showWord += '*'

    print(f'Word: {showWord}')


    if showWord == secretWord and level < 6:
        os.system('cls')
        print('YOU HAVE WON! CONGRATS!')
        print(f'Secret Word: {secretWord}.')
        print(f'Tries: {tryTimes}x.')
        level += 1
        
        tryAgain = input('Would you like to try again? (Y)es or (N)o ').lower().startswith('y')

        if tryAgain is True and level < 6:
            correctLetters = ''
            tryTimes = 0
        elif tryAgain is False and level < 6:
            proceedLevel = input(f'Would you like to proceed to LEVEL {level}? (Y)es (N)o').lower().startswith('y')

            if proceedLevel is True and level == 2:
                secretWord = 'soyeon'
                correctLetters = ''
                tryTimes = 0
            elif proceedLevel is True and level == 3:
                secretWord = 'yuqi'
                correctLetters = ''
                tryTimes = 0
            elif proceedLevel is True and level == 4:
                secretWord = 'harvey'
                correctLetters = ''
                tryTimes = 0
            elif proceedLevel is True and level == 5:
                secretWord = 'chisa'
                correctLetters = ''
                tryTimes = 0
            else:
                print('Thanks for playing!')
                break
        
        elif tryAgain is False and level > 5:
            print('Thanks for playing!')
            break