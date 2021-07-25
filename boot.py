import board
import digitalio
import storage
import usb_cdc
import usb_hid

# hold down the switch closest to usb to enable the drive
row = digitalio.DigitalInOut(board.D5)
row.switch_to_input(pull=digitalio.Pull.UP)
# note that once the drive is mounted, you can soft-reboot and it'll stay mounted
# apparently only a hard-reset causes it to be unmounted and boot.py to be read

if row.value:
    storage.disable_usb_drive()
    usb_cdc.disable()

# usb_hid.enable(devices=(usb_hid.KEYBOARD,))

row.deinit()
