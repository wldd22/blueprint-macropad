import board # type: ignore

from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.keys import KC # type: ignore
from kmk.scanners import DiodeOrientation # type: ignore

print("Starting")

keyboard = KMKKeyboard()

# 3 columns, 4 rows
keyboard.col_pins = (board.GP6, board.GP0, board.GP8)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap: rows left-to-right, top-to-bottom
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
        KC.A,  KC.N0, KC.B,
    ]
]

keyboard.rgb.set_rgb(255, 255, 255, 0)
keyboard.rgb.set_rgb(255, 255, 255, 1)
keyboard.rgb.set_rgb(255, 255, 255, 2)
keyboard.rgb.show()

if __name__ == '__main__':
    keyboard.go()
