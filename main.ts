function right () {
    basic.showLeds(`
        . . . . .
        . . . # .
        # # # # #
        . . . # .
        . . . . .
        `)
    sensors.DDMmotor(
    AnalogPin.P13,
    0,
    AnalogPin.P14,
    220
    )
    sensors.DDMmotor(
    AnalogPin.P15,
    1,
    AnalogPin.P16,
    200
    )
}
function Forward () {
    basic.showLeds(`
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . . # . .
        `)
    sensors.DDMmotor(
    AnalogPin.P13,
    0,
    AnalogPin.P14,
    255
    )
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    255
    )
}
function UnCatch () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.servoWritePin(AnalogPin.P12, 180)
}
function left () {
    basic.showLeds(`
        . . . . .
        . # . . .
        # # # # #
        . # . . .
        . . . . .
        `)
    sensors.DDMmotor(
    AnalogPin.P13,
    1,
    AnalogPin.P14,
    220
    )
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    220
    )
}
function stop () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        `)
    sensors.DDMmotor(
    AnalogPin.P13,
    1,
    AnalogPin.P14,
    0
    )
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    0
    )
}
function Stop2 () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.servoWritePin(AnalogPin.P12, 90)
}
function Catch () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.servoWritePin(AnalogPin.P12, 0)
}
function Backward () {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        . . # . .
        `)
}
