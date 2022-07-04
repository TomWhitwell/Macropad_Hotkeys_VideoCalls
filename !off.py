from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'OFF', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', [Keycode.COMMAND, Keycode.SHIFT, 'a']),
        (0x000000, '', [ConsumerControlCode.VOLUME_INCREMENT]),
        (0x000000, '', [ConsumerControlCode.VOLUME_DECREMENT]),
        # 2nd row ----------
        (0x000000, '', [Keycode.COMMAND, Keycode.SHIFT, 'v']),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', [Keycode.OPTION,'y']),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
