from sense_hat import SenseHat
import random

sense = SenseHat()

blue = (0, 0, 255)
nothing = (0, 0, 0)


def rollAdice(sides):
    return random.randint(1, sides)


while True:
    try:
        numberOfFaces = int(input('How many faces you dice will have: '))
        if numberOfFaces < 1 or numberOfFaces > 64:
            print('Please enter a number between 1 and 64')
            continue
    except ValueError:
        print('Please enter a valid integer')
        continue
    while True:

        listColor = []
        face = rollAdice(numberOfFaces)
        print('The random value is : {}'.format(face))
        for i in range(face):
            listColor.append(blue)
        for i in range(64 - face):
            listColor.append(nothing)
        sense.set_pixels(listColor)
        tryAgain = input('Do you want to roll the dice again? y/n ')
        if tryAgain == 'n':
            break
    break

print('Your done, Thank you')







