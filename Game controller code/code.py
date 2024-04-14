import time
from display_control import DisplayController  # Import the DisplayController class from display_control.py
import board
import usb_hid
from buttons import Buttons
from weapon_scroll import WeaponScroll
from joystick import Joystick
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode
import asyncio

keyboard = Keyboard(usb_hid.devices)
joystick = Joystick(board.GP27, board.GP28, keyboard)
weaponScroll = WeaponScroll(board.GP26)
buttons = Buttons([board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22], keyboard, [Keycode.TAB, Keycode.PERIOD, Keycode.COMMA, Keycode.SPACE, Keycode.CONTROL, Keycode.ENTER, Keycode.ESCAPE])
display_controller = DisplayController()

#display_controller.update_from_file("welcome.txt")
#time.sleep(2)
#display_controller.update_from_file("names.txt")
#time.sleep(1)

def file_content_changed(filepath, last_content):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        if content != last_content:
            return True, content
        return False, last_content
    except OSError:
        return False, last_content

async def handle_inputs():
    while True:
        joystick.read()
        key_code = weaponScroll.read()
        if key_code is not None:
            keyboard.press(key_code)
            await asyncio.sleep(0.1)  # Add a delay to register key press
            keyboard.release(key_code)
        buttons.read()
        joystick.release_joystick()
        await asyncio.sleep(0) 
    
    # Check if it's time to upate the display (every 1 second)
async def update_displays():
    last_content = ""
    while True:
        changed, last_content = file_content_changed("player_stats.txt", last_content)
        if changed:
            display_controller.update_from_file("player_stats.txt")
        await asyncio.sleep(2)

loop = asyncio.get_event_loop()
loop.create_task(handle_inputs())
loop.create_task(update_displays())
loop.run_forever()
# 33333330007