def right():
    basic.show_leds("""
        . . . . .
        . . . # .
        # # # # #
        . . . # .
        . . . . .
        """)
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 220)
    sensors.dd_mmotor(AnalogPin.P15, 1, AnalogPin.P16, 200)
def Forward():
    basic.show_leds("""
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . . # . .
        """)
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 255)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 255)
def UnCatch():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.servo_write_pin(AnalogPin.P12, 180)
def left():
    basic.show_leds("""
        . . . . .
        . # . . .
        # # # # #
        . # . . .
        . . . . .
        """)
    sensors.dd_mmotor(AnalogPin.P13, 1, AnalogPin.P14, 220)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 220)
def stop():
    basic.show_leds("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """)
    sensors.dd_mmotor(AnalogPin.P13, 1, AnalogPin.P14, 0)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 0)
def Stop2():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.servo_write_pin(AnalogPin.P12, 90)
def Catch():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.servo_write_pin(AnalogPin.P12, 0)
def Backward():
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        . . # . .
        """)

def diver():
    if (pins.digital_read_pin(DigitalPin.P1) == 0 and pins.digital_read_pin(DigitalPin.P8) == 0):
        forward()
    elif (pins.digital_read_pin(DigitalPin.P1) == 1 and pins.digital_read_pin(DigitalPin.P8) == 0):
        while (pins.digital_read_pin(DigitalPin.P1) == 1):
            left()
    elif (pins.digital_read_pin(DigitalPin.P1) == 0 and pins.digital_read_pin(DigitalPin.P8) == 1):
        while (pins.digital_read_pin(DigitalPin.P8) == 1):
            right()
    elif (pins.digital_read_pin(DigitalPin.P1) == 1 and pins.digital_read_pin(DigitalPin.P8) == 1):
        pass
    else : 
    basic.show_leds("""
    . # . . .
    . . # . .
    . . # . .
    . . . # .
    . . . # .
    """)
    return 0

def NLeft():
    stop()
    pause(300)
    forward()
    pause(200)
    while pins.digital_read_pin(DigitalPin.P1) == 0:
        left()
    stop()
    pause(100)
    while pins.digital_read_pin(DigitalPin.P1) == 1:
        left()
    stop()
    pause(100)
    return 0

def NRight():
    stop()
    pause(300)
    while pins.digital_read_pin(DigitalPin.P1) == 0:
        right()
    stop()
    pause(100)
    while pins.digital_read_pin(DigitalPin.P1) == 1:
        right()
    stop()
    pause(100)
    return 0



def event(num):
    if num == 1:
        NLeft()
    else basic.show_string("No event left")
    
