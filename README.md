# Adafruit-MacroPad-RP2040-MIDI-Piano

CircuitPy source for using the Adafruit MacroPad RP2040 as a MIDI Piano over USB.

## Versions

This code was written and used with:

- CircuitPy 8.0.0-alpha.1 `adafruit-circuitpython-adafruit_macropad_rp2040-en_US-8.0.0-alpha.1`

## References

- [DevDungeon MacroPad Tutorial](https://www.devdungeon.com/content/adabox-019-macropad)
- [MacroPad Firmware Download](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython)
- [CircuitPy Library Collection](https://circuitpython.org/libraries)

## Setup

To get into bootloader mode on the MacroPad, press and hold the rotary encoder
button when resetting. Then it will show up as removable drive `RPI-RP2`.
That's when you can drop a `.uf2` firmware file, whether updated device firmware,
the [nuke firmware](https://cdn-learn.adafruit.com/assets/assets/000/101/659/original/flash_nuke.uf2?1618945856), or the [MacroPad CircuitPy firmware](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython).

After CircuitPy firmware is installed, the removable drive should show up as `CIRCUITPY`.
Then copy the files inside the `dist/` folder (but not the dist folder itself) to the device.
The `code.py` file should sit in the root of the `CIRCUITPY` drive next to a `libs/` dir.

## Usage

The device will play act as a MIDI piano with only C-minor pentatonic scale playable.