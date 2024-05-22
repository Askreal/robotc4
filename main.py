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

def Backward():
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        . . # . .
        """)

def Catch():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.servo_write_pin(AnalogPin.P12, 0)

def UnCatch():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.servo_write_pin(AnalogPin.P12, 180)


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

    