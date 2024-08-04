from kb import KMKKeyboard

from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers
from kmk.keys import KC




keyboard = KMKKeyboard()

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)
# Enable split keyboard functionality
split = Split(
    split_type=SplitType.UART,
    data_pin=keyboard.data_pin,
    uart_flip=True,
    use_pio=True,
    split_side=SplitSide.LEFT,
)

# Layers definition
keyboard.modules.append(Layers())
keyboard.modules.append(split)

# Define keymap
from kmk.keys import KC
keyboard.keymap = [
    [  # BASE
        KC.ESC,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,   KC.I,    KC.O,    KC.P, KC.BSPC,
        KC.TAB,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,   KC.K,    KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.ENT,
                                      KC.LCTL, KC.LGUI, KC.SPC,   KC.LALT,   KC.RALT, KC.RCTL,  KC.RSFT,
    ],
    [  # LOWER
        KC.NO, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                   KC.LGUI,   LOWER,  ADJUST, XXXXXXX,      XXXXXXX,  KC.ENT,   RAISE,  KC.RALT,
    ],
    [  # RAISE
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,
                                   KC.LGUI,   LOWER,  ADJUST, XXXXXXX,      XXXXXXX,  KC.ENT,   RAISE,  KC.RALT,
    ],
    [  # ADJUST
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                   KC.LGUI,   LOWER,  ADJUST, XXXXXXX,      XXXXXXX,  KC.ENT,   RAISE,  KC.RALT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
