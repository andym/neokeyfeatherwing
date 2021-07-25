""" Use the adafruit neokey featherwing and the rp2040 feather to make a little macropad """
import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import neopixel
import keypad
import adafruit_logging as logging


class Pixels:
    """Manage the 2 whole neopixels on the board. We do a nice flash on init. """

    def __init__(self):
        pixel_pin = board.D9

        self.colours = {
            "white": 0xCCCCCC,
            "black": 0x000000,
            "yellow": 0xFFF900,
            "orange": 0xFF5A00,
        }
        self.pixels = neopixel.NeoPixel(pixel_pin, 2, brightness=1.0)
        self.pixels.fill(self.colours["black"])
        time.sleep(0.3)
        self.pixels.fill(self.colours["white"])
        time.sleep(0.3)
        self.pixels.fill(self.colours["black"])

    def make_a(self, colour):
        self.pixels[0] = self.colours[colour]

    def make_b(self, colour):
        self.pixels[1] = self.colours[colour]


class TwoPercent:
    """Class for the adafruit neokey featherwing. Uses the keypad module. """

    def __init__(self):
        self.logger = logging.getLogger("keypad")
        self.logger.setLevel(logging.INFO)

        self.pixels = Pixels()

        self.keyboard = Keyboard(usb_hid.devices)

        self.k = keypad.Keys((board.D5, board.D6), value_when_pressed=False, pull=True)

        a_pressed = keypad.Event(0, True)
        a_released = keypad.Event(0, False)
        b_pressed = keypad.Event(1, True)
        b_released = keypad.Event(1, False)

        self.dispatch = {
            a_pressed: self.a_pressed,
            a_released: self.a_released,
            b_pressed: self.b_pressed,
            b_released: self.b_released,
        }

        self.logger.info("Keypad ready.")

    # These methods make
    #   button A press / release space and go yellow
    #   button B press F18 (wait a bit) H and go an orange-that-looks-yellowish
    #   F18..H is mapped using karabiner to "focus chrome"
    def a_pressed(self):
        self.pixels.make_a("yellow")
        self.keyboard.press(Keycode.SPACEBAR)

    def a_released(self):
        self.pixels.make_a("black")
        self.keyboard.release(Keycode.SPACEBAR)

    def b_pressed(self):
        self.pixels.make_b("orange")
        self.keyboard.press(Keycode.F18)
        time.sleep(0.3)
        self.keyboard.press(Keycode.H)

    def b_released(self):
        self.pixels.make_b("black")
        self.keyboard.release(Keycode.H)
        self.keyboard.release(Keycode.F18)

    def loop(self):
        while True:
            k_event = self.k.events.get()
            if k_event:
                self.logger.info(str(k_event))
                self.dispatch[k_event]()


def main():
    two = TwoPercent()
    two.loop()


if __name__ == "__main__":
    main()
