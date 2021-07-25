This is a small [circuitpython](https://circuitpython.org) project to demonstate my workflow.

It runs on an [adafruit rp2040 feather](https://www.adafruit.com/product/4884) with a
[neokey featherwing](https://www.adafruit.com/product/4979) attached.

I used [this guide](https://learn.adafruit.com/deco-two-key-keypad-macropad-circuitpython-feather/code-the-deco-keypad) for inspiration, which has the stl for a nice 3d printable case.

I'm using the new (as of circuitpython 7) [keypad](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython) module, which makes handling of keys a breeze.

[boot.py](boot.py) also uses new circuitpython 7 features to turn off the storage device. If you want to edit or
update the code on the board, hold down the switch nearest the usb port when powering it up.
When you update the code it does a soft-reset, which doesn't run boot.py again, so the feather is still
visible as a drive until you unmount it and do a proper reset.

The workflow requires you to have [circup](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup) installed.

Once you've done that, plug your board in and run [install.sh](install.sh). We check the board looks like the
right one, we run circup to install the [necessary libraries](board_requirements.txt), we copy boot.py and lastly code.py which
causes the device to do a soft reboot.

You can now edit the code in whichever editor you choose, commit your changes to git and manage your
dependencies properly, which lets you nuke a board and start again from scratch very easily.

The actual key macros are probably only useful to me - they'e shortcuts for Jitsi - push to talk and push to focus chrome.
