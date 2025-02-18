import random


def guessNumber():

    guessedNumber = random.randrange(1, 100)
    #print(guessedNumber)
    userNumber = ''

    while userNumber != guessedNumber:
        userNumber = input('Podaj liczbe: ')
        if userNumber < guessedNumber:
            print('Zgadywana liczba jest wieksza')
        elif userNumber > guessedNumber:
            print('Zgadywana liczba jest mniejsza')
        else:
            print('Gratulacje trafiles liczbe.')

guessNumber()