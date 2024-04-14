import digitalio
from adafruit_hid.keyboard import Keyboard, Keycode

class Buttons:
    def __init__(self, pins, keyboard, keycodes):
        self.buttons = [digitalio.DigitalInOut(pin) for pin in pins]
        for button in self.buttons:
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.UP
        self.keyboard = keyboard
        self.button_keycodes = keycodes

    def read(self):
        for i, button in enumerate(self.buttons):
            if not button.value:
                self.keyboard.press(self.button_keycodes[i])
            else:
                self.keyboard.release(self.button_keycodes[i])
