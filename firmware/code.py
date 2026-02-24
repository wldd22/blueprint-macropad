import board

print("Starting")

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
        KC.A,  KC.N0, KC.B,
    ]
]

# keyboard.rgb.set_rgb(255, 255, 255, 0)
# keyboard.rgb.set_rgb(255, 255, 255, 1)
# keyboard.rgb.set_rgb(255, 255, 255, 2)
# keyboard.rgb.show()

if __name__ == '__main__':
    keyboard.go()
