imagesListIndex = 0
imagesList: List[Image] = []
strip: neopixel.Strip = None

while True:
    if input.logo_is_pressed():
        if smarthome.PIR(DigitalPin.P0):
            basic.show_string("presence has been detected")
            basic.clear_screen()
        else:
            basic.show_string("no presence has been detected")
            basic.clear_screen()
    elif input.is_gesture(Gesture.SHAKE):
        basic.show_number(smarthome.read_soil_humidity(AnalogPin.P0))
        basic.clear_screen()
        serial.write_value("moisture", smarthome.read_soil_humidity(AnalogPin.P0))
    elif input.pin_is_pressed(TouchPin.P0):
        basic.show_number(smarthome.uv_level(AnalogPin.P0))
        basic.clear_screen()
    elif input.pin_is_pressed(TouchPin.P1):
        basic.show_number(smarthome.uv_level(AnalogPin.P1))
        basic.clear_screen()
    elif input.pin_is_pressed(TouchPin.P2):
        basic.show_number(smarthome.uv_level(AnalogPin.P2))
        basic.clear_screen()
    elif input.button_is_pressed(Button.A):
        basic.show_number(input.temperature())
        basic.clear_screen()
        serial.write_value("temperature", input.temperature())
    elif input.button_is_pressed(Button.B):
        basic.show_number(input.light_level())
        basic.clear_screen()
        serial.write_value("brightness", input.light_level())
        if input.light_level() < 35:
            basic.show_string("too dark")
            basic.clear_screen()
        elif input.light_level() < 135:
            basic.show_string("too light")
            basic.clear_screen()

def on_forever():
    global strip, imagesList, imagesListIndex
    strip = neopixel.create(DigitalPin.P8, 24, NeoPixelMode.RGB)
    strip.show_rainbow(1, 360)
    imagesList = [images.icon_image(IconNames.HAPPY),
        images.icon_image(IconNames.SAD),
        images.icon_image(IconNames.CONFUSED),
        images.icon_image(IconNames.ANGRY),
        images.icon_image(IconNames.SURPRISED),
        images.icon_image(IconNames.SILLY),
        images.icon_image(IconNames.MEH),
        images.icon_image(IconNames.DUCK),
        images.icon_image(IconNames.TORTOISE),
        images.icon_image(IconNames.BUTTERFLY),
        images.icon_image(IconNames.GIRAFFE),
        images.icon_image(IconNames.SNAKE),
        images.icon_image(IconNames.RABBIT),
        images.icon_image(IconNames.COW)]
    imagesListIndex = 0
    while imagesListIndex <= len(imagesList) - 1:
        imagesList[imagesListIndex].show_image(0)
        imagesListIndex += 1
basic.forever(on_forever)
