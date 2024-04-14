import analogio
from adafruit_hid.keyboard import Keycode

class WeaponScroll:
    def __init__(self, pin):
        self.potentiometer = analogio.AnalogIn(pin)
        self.prev_pot_state = None

    def read(self):
        pot_value = 65535 - self.potentiometer.value
        button_ranges = [
            (0, 9362, Keycode.ZERO),
            (9363, 18725, Keycode.TWO),
            (18726, 28087, Keycode.THREE),
            (28088, 37449, Keycode.FOUR),
            (37450, 46811, Keycode.FIVE),
            (46812, 56173, Keycode.SIX),
            (56174, 65535, Keycode.SEVEN)
        ]

        current_button = None
        for start, end, keycode in button_ranges:
            if start <= pot_value <= end:
                current_button = keycode
                break

        if current_button != self.prev_pot_state:
            self.prev_pot_state = current_button
            return current_button

        return None
