import board
import busio
import digitalio
import time
from lcd.lcd import LCD, CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from adafruit_ht16k33 import matrix

class DisplayController:
    def __init__(self):
        
        # Initialize the LED matrix and LCD using I2C
        i2c = busio.I2C(board.GP15, board.GP14)  # SDA = GP4, SCL = GP5
        i2c_2 = busio.I2C(board.GP5,board.GP4)
        
        # Initialize the LCD 
        interface = I2CPCF8574Interface(i2c, 0x27)
        self.lcd = LCD(interface,16,2)
        self.lcd.set_cursor_mode(CursorMode.HIDE)
        
        # Initialize the matrix
        self.led_matrix = matrix.Matrix8x8(i2c_2)
    
    def update_display(self, mood):
        # Define face patterns
        happy = [
            0b00000000,
            0b00111100,
            0b01000010,
            0b01111110,
            0b00000000,
            0b01100110,
            0b01100110,
            0b00000000
        ]
        neutral = [
            0b00000000,
            0b00111100,
            0b01000010,
            0b00000000,
            0b00000000,
            0b01100110,
            0b01100110,
            0b00000000
        ]
        sad = [
            0b00000000,
            0b00000000,
            0b01000010,
            0b00111100,
            0b00000000,
            0b01100110,
            0b01100110,
            0b00000000
        ]
        skull = [
            0b11111111,
            0b11100111,
            0b10000001,
            0b11011011,
            0b11111111,
            0b10011001,
            0b10111101,
            0b11111111
            ]

        # Update the LED matrix with the selected face
        face = happy if mood == "happy" else neutral if mood == "neutral" else sad 
        self.led_matrix.fill(0)
        for y, row in enumerate(face):
            for x in range(8):
                self.led_matrix.pixel(x, y, 1 << x & row)
        self.led_matrix.show()

    def update_from_file(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
        if len(lines) < 3:
            line1=lines[0].strip('\n')
            line2=lines[1].strip('\n')
            
            self.lcd.clear()
            self.lcd.print(f"{line1}\n{line2}\n")
            
        
        if len(lines) >= 3:
            health = int(lines[0].split(':')[1].strip())
            armor = lines[1].strip()
            kills = lines[2].strip()

            # Set the LCD message to show stats
            self.lcd.clear()
            self.lcd.print(f"{armor}\n{kills}")
            
            mood = "happy" if health >= 100 else "neutral" if 50 <= health < 100 else "sad"
            self.update_display(mood)
