board.D0,
    board.D1,
    None,  # GND
    None,  # GND
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,
    board.D8,
    board.D9,
    board.D10,
    board.MOSI,
    board.MISO,
    board.SCK,
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    None,  # 3.3v
    None,  # RST
    None,  # GND
    None,  

import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.kb2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [MatrixScanner(
            # required arguments:
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )]
    col_pins = (
        board.pins[17],
        board.pins[16],
        board.pins[15],
        board.pins[14],
        board.pins[13],
        board.pins[12],
    )
    row_pins = (
        board.pins[7],
        board.pins[8],
        board.pins[9],
        board.pins[10],
        board.pins[11],
    )
    diode_orientation = DiodeOrientation.COLUMNS
    uart_pin = board.pins[1]  # Correct UART pin, adjust if necessary
    rgb_pixel_pin = None  # No RGB support
    data_pin = board.pins[1] # Assuming UART split is used on GP1
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

