import analogio
from adafruit_hid.keyboard import Keyboard, Keycode

class Joystick:
    NEUTRAL_POSITION = 33000
    THRESHOLD = 15000

    def __init__(self, x_pin, y_pin, keyboard):
        self.joystick_x = analogio.AnalogIn(x_pin)
        self.joystick_y = analogio.AnalogIn(y_pin)
        self.keyboard = keyboard
        self.joystick_pressed = {"left": False, "right": False, "up": False, "down": False}

    def read(self):
        x_position = self.joystick_x.value
        y_position = self.joystick_y.value

        # Right (previously left)
        if x_position < self.NEUTRAL_POSITION - self.THRESHOLD and not self.joystick_pressed["right"]:
            self.keyboard.press(Keycode.RIGHT_ARROW)
            self.joystick_pressed["right"] = True
        elif x_position > self.NEUTRAL_POSITION - self.THRESHOLD and self.joystick_pressed["right"]:
            self.keyboard.release(Keycode.RIGHT_ARROW)
            self.joystick_pressed["right"] = False

        # Left (previously right)
        if x_position > self.NEUTRAL_POSITION + self.THRESHOLD and not self.joystick_pressed["left"]:
            self.keyboard.press(Keycode.LEFT_ARROW)
            self.joystick_pressed["left"] = True
        elif x_position < self.NEUTRAL_POSITION + self.THRESHOLD and self.joystick_pressed["left"]:
            self.keyboard.release(Keycode.LEFT_ARROW)
            self.joystick_pressed["left"] = False

        # Down
        if y_position > self.NEUTRAL_POSITION + self.THRESHOLD and not self.joystick_pressed["down"]:
            self.keyboard.press(Keycode.DOWN_ARROW)
            self.joystick_pressed["down"] = True
        elif y_position < self.NEUTRAL_POSITION + self.THRESHOLD and self.joystick_pressed["down"]:
            self.keyboard.release(Keycode.DOWN_ARROW)
            self.joystick_pressed["down"] = False

        # Up
        if y_position < self.NEUTRAL_POSITION - self.THRESHOLD and not self.joystick_pressed["up"]:
            self.keyboard.press(Keycode.UP_ARROW)
            self.joystick_pressed["up"] = True
        elif y_position > self.NEUTRAL_POSITION - self.THRESHOLD and self.joystick_pressed["up"]:
            self.keyboard.release(Keycode.UP_ARROW)
            self.joystick_pressed["up"] = False

    def release_joystick(self):
        # Release all joystick keys
        for direction in self.joystick_pressed:
            if self.joystick_pressed[direction]:
                if direction == "left":
                    self.keyboard.release(Keycode.LEFT_ARROW)
                elif direction == "right":
                    self.keyboard.release(Keycode.RIGHT_ARROW)
                elif direction == "up":
                    self.keyboard.release(Keycode.UP_ARROW)
                elif direction == "down":
                    self.keyboard.release(Keycode.DOWN_ARROW)
                self.joystick_pressed[direction] = False