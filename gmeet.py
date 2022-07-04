from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Google Meet', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'MUTE', [Keycode.COMMAND, 'd']),
        (0x000000, '', []),
        (0x202020, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 2nd row ----------
        (0x202020, 'Vid', [Keycode.COMMAND, 'e']),
        (0x000000, '', []),
        (0x202020, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x202020, 'Hand', [Keycode.CONTROL, Keycode.COMMAND, 'h']),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
