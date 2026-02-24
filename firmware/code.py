import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
layers_ext = Layers()

keyboard.modules.append(layers_ext)

# Define hardware pins
keyboard.col_pins = (board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Keymap setup:
# Layer 0 = default
# Layer 1 = F13...F23 outputs if the modifier key is held

keyboard.keymap = [
    # LAYER 0 – default
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
        KC.MO(1), KC.N0, KC.BSPC,
    ],

    # LAYER 1 – F13–F23 when modifier held
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
        KC.F19, KC.F20, KC.F21,
        KC.TRNS, KC.F22, KC.F23,
    ]
]

if __name__ == "__main__":
    keyboard.go()