import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.kb2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    )
    row_pins = (
        board.D5,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    uart_pin = board.D1  # Correct UART pin, adjust if necessary
    rgb_pixel_pin = None  # No RGB support
    data_pin = board.D1  # Assuming UART split is used on GP1
    i2c = board.I2C

    coord_mapping = [
     0,  1,  2,  3,  4,  5,  35, 34, 33, 32, 31, 30,
     6,  7,  8,  9, 10, 11,  41, 40, 39, 38, 37, 36,
    12, 13, 14, 15, 16, 17,  47, 46, 45, 44, 43, 42,
    18, 19, 20, 21, 22, 23,  53, 52, 51, 50, 49, 48,
        25, 26, 27, 28, 29,  59, 58, 57, 56, 55,
    ]
     # flake8: noqa
    # fmt: off

# MatrixScanner for scanning key matrix
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        super().__init__()
        self.matrix = MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            columns_to_anodes=self.diode_orientation,
        )

keyboard = MyKeyboard()