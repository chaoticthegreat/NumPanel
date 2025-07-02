
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1, board.D26, board.D27, board.D28, board.D29]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.RIGHT, KC.LEFT, KC.UP, KC.DOWN, KC.ENTER, KC.ESC, KC.BSPC, KC.TAB],
]
if __name__ == '__main__':
    keyboard.go()