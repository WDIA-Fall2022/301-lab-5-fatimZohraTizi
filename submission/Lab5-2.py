from sense_hat import SenseHat
import random

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 128, 255)
dark_blue = (0, 0, 153)
green = (0, 102, 0)
light_green = (0, 255, 0)
nothing = (0,0,0)

#Program to display temperature

def displayColorForTemperature(temperature):
    temp = round(temperature)
    if temp >= -40 and temp <= -10:
        sense.clear(dark_blue)
    elif temp >= -9 and temp <= 0:
        sense.clear(blue)
    elif temp >= 1 and temp <= 15:
        sense.clear(light_green)
    elif temp >= 16 and temp <= 22:
        sense.clear(green)
    elif temp >= 23:
        sense.clear(red)


while True:
    temp = float(random.randint(-40, 60))
    print(temp)
    displayColorForTemperature(temp)
    tryAgain = input('Try again? y/n ')
    if tryAgain == 'n':
        break


#Program to display humidity

def LedsOnForHumidity(humidity):
    listColor = []
    humLed = round(round(humidity * 0.64) / 8) * 8
    for i in range(humLed):
        listColor.append(blue)
    for i in range(64 - humLed):
        listColor.append(nothing)
    sense.set_pixels(listColor)


while True:
    humidity = int(random.randint(0, 100))
    print(humidity)
    LedsOnForHumidity(humidity)
    tryAgain = input('Try again? y/n ')
    if tryAgain == 'n':
        break








    
    
