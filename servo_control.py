from pyfirmata import Arduino, SERVO
from time import sleep

# the port the arduino is connected to(will update to get it programatically)
port = 'COM4'


hand1 = 3
hand2 = 5
lift = 7

board = Arduino(port)

board.digital[hand1].mode = SERVO
board.digital[hand2].mode = SERVO
board.digital[lift].mode = SERVO


# Raises the lift
def raiseLift():
    for i in range(35, 135):
        board.digital[lift].write(i)
        sleep(0.015)

# Lowers the lift


def lowerLift():
    for i in range(135, 35, -1):
        board.digital[lift].write(i)
        sleep(0.015)

# Raises first hand


def raiseFirstHand():
    for i in range(35, 135):
        board.digital[hand1].write(i)
        sleep(0.015)

# Lowers first hand


def lowerFirstHand():
    for i in range(135, 35, -1):
        board.digital[hand1].write(i)
        sleep(0.015)

# Raises second hand


def raiseSecondHand():
    for i in range(0, 110):
        board.digital[hand2].write(i)
        sleep(0.015)

# Lowers second hand


def lowerSecondHand():
    for i in range(110, 0, -1):
        board.digital[hand2].write(i)
        sleep(0.015)
