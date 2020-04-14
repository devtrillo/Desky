# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 144*2

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER, brightness=1
)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


def color_fill(color, max_pixels=40):
    max_num_pixels = max_pixels if max_pixels < num_pixels else num_pixels
    for i in range(max_num_pixels):
        pixels[i] = color
    pixels.show()


def rainbow(max_pixels=40):
    max_num_pixels = max_pixels if max_pixels < num_pixels else num_pixels
    for i in range(max_num_pixels):
        pixels[i] = wheel((int(i * 256 / num_pixels)) & 255)
    pixels.show()


def rainbow_cycle(max_pixels=40, iteration=0):
    max_num_pixels = max_pixels if max_pixels < num_pixels else num_pixels
    for i in range(max_num_pixels):
        pixel_index = (i * 256 // num_pixels) + iteration
        pixels[i] = wheel(pixel_index & 255)
    pixels.show()


def theather_chase(color, iteration=0, max_pixels=40):
    max_num_pixels = max_pixels if max_pixels < num_pixels else num_pixels
    q = iteration % 4
    for i in range(0, max_num_pixels, 3):
        if i+q < max_num_pixels:
            pixels[i+q] = color
    pixels.show()
    for i in range(0, max_num_pixels, 3):
        if i+q < max_num_pixels:
            pixels[i+q] = (0, 0, 0)


def rainbow_theather_chase(iteration=0, max_pixels=40):
    j = iteration % 256
    max_num_pixels = max_pixels if max_pixels < num_pixels else num_pixels

    for q in range(3):
        for i in range(0, max_num_pixels, 3):
            pixels[i+q] = wheel((i+j) % 255)
        pixels.show()
        for i in range(0, max_num_pixels, 3):
            pixels[i+q] = (0, 0, 0)
