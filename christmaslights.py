#!/usr/bin/python

# Christmas Wreath Project
# Author: Eric Littler (ericlittler@yahoo.com)
#
# -Port of the Arduino NeoPixel library strandtest example (Adafruit).
# -Uses the WS2811 to animate RGB light strings (I am using a 5V, 50x RGB LED strand)
# -This will provide a light sequence for a strand of lights wrapped around a wreath


# Import libs used
import time
import random
from neopixel import *
import os

#Start up random seed
random.seed()

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#Predefined Colors and Masks
OFF = Color(0,0,0)
BLACK = Color(0,0,0)
WHITE = Color(255,255,255)
RED = Color(255,0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)
PURPLE = Color(128,0,128)
YELLOW = Color(255,255,0)
ORANGE = Color(255,50,0)
TURQUOISE = Color(64,224,208)
RANDOM = Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

#list of colors, tried to match the show as close as possible
COLORS = [YELLOW,GREEN,RED,BLUE,ORANGE,TURQUOISE,GREEN,
          YELLOW,PURPLE,RED,GREEN,BLUE,YELLOW,RED,TURQUOISE,GREEN,RED,BLUE,GREEN,ORANGE,
          YELLOW,GREEN,RED,BLUE,ORANGE,TURQUOISE,RED,BLUE, 
          ORANGE,RED,YELLOW,GREEN,PURPLE,BLUE,YELLOW,ORANGE,TURQUOISE,RED,GREEN,YELLOW,PURPLE,
          YELLOW,GREEN,RED,BLUE,ORANGE,TURQUOISE,GREEN,BLUE,ORANGE] 

#bitmasks used in scaling RGB values
REDMASK = 0b111111110000000000000000
GREENMASK = 0b000000001111111100000000
BLUEMASK = 0b000000000000000011111111

# Other vars
ALPHABET = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYy'  #alphabet that will be used (irrelevant--just filling it with 50 letters for now)
LIGHTSHIFT = 0  #shift the lights down the strand to the other end 
FLICKERLOOP = 3  #number of loops to flicker

def initLights(strip):
  """
  initializes the light strand colors 

  inputs:
    strip = color strip instance to action against

  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize all LEDs
  for i in range(len(ALPHABET)):
    strip.setPixelColor(i+LIGHTSHIFT, COLORS[i%colorLen])
  strip.show()

def lightNone(strip):
  """
  turns off all lights

  inputs:
    strip = color strip instance to action against
	colors = a 50 length array of colors with which to light the wreath
	
  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize all LEDs
  for i in range(len(ALPHABET)):
    strip.setPixelColor(i+LIGHTSHIFT, BLACK)
  strip.show()
  
def lightAll(strip, colors):
  """
  light the strand all at once

  inputs:
    strip = color strip instance to action against
	colors = a 50 length array of colors with which to light the wreath
	
  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize all LEDs at once
  for i in range(len(ALPHABET)):
    strip.setPixelColor(i+LIGHTSHIFT, COLORS[i%colorLen])
  strip.show()

def lightSequential(strip, colors):
  """
  light the strand sequentially

  inputs:
    strip = color strip instance to action against
	colors = a 50 length array of colors with which to light the wreath
	
  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize LEDs one by one
  for i in range(len(ALPHABET)):
    strip.setPixelColor(i+LIGHTSHIFT, COLORS[i%colorLen])
	strip.show()
	time.sleep(0.75)

def lightRandom(strip, colors):
  """
  light the strand randomly

  inputs:
    strip = color strip instance to action against
	colors = a 50 length array of colors with which to light the wreath
	
  outputs:
    <none>
  """
  colorLen = len(COLORS)
  #Initialize LEDs one by one

  for i in range(len(ALPHABET)):
    strip.setPixelColor(s[i]+LIGHTSHIFT, COLORS[s[i]%colorLen])
    strip.show()
    time.sleep(random.randint(10,80)/1000.0)

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
  strip.begin()

  #print ('Type q to quit.')

  os.system('clear')
  print "Type your message (q to quit) and press Enter:"
  userInput = raw_input()
  lightNone(strip)
  time.sleep(1)
  COLORS = [WHITE] * 50
  lightAll(strip, COLORS)
  lightNone(strip)
  time.sleep(1)
  COLORS = [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
			WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
			WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
			WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
			WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE] 
  lightSequential(strip, COLORS)
  lightNone(strip)
  time.sleep(1)
  COLORS = [RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE,
			RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE,
			RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE,
			RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE, RED, GREEN, WHITE,
			RED, GREEN]
  lightRandom(strip, COLORS)
  time.sleep(1)
  COLORS = [RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED] 
  lightSequential(strip, COLORS)
  time.sleep(1)
  COLORS = [GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN] 
  lightSequential(strip, COLORS)
  time.sleep(1)
  COLORS = [RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED,
			RED, RED, RED, RED, RED, RED, RED, RED, RED, RED] 
  lightSequential(strip, COLORS)
  time.sleep(1)
  COLORS = [GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
			GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN] 
  lightSequential(strip, COLORS)
  time.sleep(1)
  lightNone(strip)

print 'Merry Christmas...'
time.sleep(2)
os.system('clear')
