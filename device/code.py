"""
G9 = 127
"A4" = 69
C4 = 60
C0 = 12
"""
from adafruit_macropad import MacroPad

# C minor pentatonic
SCALE = [60, 63, 65, 67, 70, 72, 74, 77, 79, 82, 84, 87] # C4 minor pentatonic (1 b3 4 5 b7)
# D# minor pentatonic
SCALE = [63, 66, 68, 70, 73, 75, 77, 80, 82, 85, 87, 90] # C4 minor pentatonic (1 b3 4 5 b7)
# C minor pentatonic shuffled
#SCALE = [72, 63, 79, 77,84, 65, 60,67, 70,82,  74,   87]

macropad = MacroPad()

lines = macropad.display_text(title="Dano's MIDI pad") # First line
lines[0].text = 'C minor pentatonic'  # Second line
lines[1].text = 'Red = root'  # Third line
lines[2].text = 'Orange = 5th'  # Fourth line
lines.show() # Only required the first time?

# NeoPixels
macropad.pixels.brightness = 0.2 # up to 1
macropad.pixels.fill((0, 255, 255))
# Roots
macropad.pixels[0] = (255, 0, 0)
macropad.pixels[5] = (255, 0, 0)
macropad.pixels[10] = (255, 0, 0)
# Fifths
macropad.pixels[3] = (255, 128, 0)
macropad.pixels[8] = (255, 128, 0)

# Keypress detection
while True:

    # Key buttons (poll for events)
    event = macropad.keys.events.get()
    while event:
        if event.pressed:
            macropad.midi.send(macropad.NoteOn(SCALE[event.key_number], 99))
        elif event.released:
            macropad.midi.send(macropad.NoteOff(SCALE[event.key_number], 0))
        # Check for other key events too
        event = macropad.keys.events.get()

