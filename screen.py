#!/usr/bin/env python3

# Script to communicate with a serial device (LCD)

import serial, math
import time

# 'serial' for serial communication

# COMMANDS
# from lcd_comm_rev_c.py
# Command sequences represented as bytearrays
HELLO = bytearray((0x01, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0xc5, 0xd3))
OPTIONS = bytearray((0x7d, 0xef, 0x69, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x2d))
RESTART = bytearray((0x84, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))
TURNOFF = bytearray((0x83, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))
TURNON = bytearray((0x83, 0xef, 0x69, 0x00, 0x00, 0x00, 0x00))

SET_BRIGHTNESS = bytearray((0x7b, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00))

# STOP COMMANDS
STOP_VIDEO = bytearray((0x79, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))
STOP_MEDIA = bytearray((0x96, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))

# IMAGE QUERY STATUS
QUERY_STATUS = bytearray((0xcf, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))

# STATIC IMAGE
START_DISPLAY_BITMAP = bytearray((0x2c,))
PRE_UPDATE_BITMAP = bytearray((0x86, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))
UPDATE_BITMAP = bytearray((0xcc, 0xef, 0x69, 0x00))

RESTARTSCREEN = bytearray((0x84, 0xef, 0x69, 0x00, 0x00, 0x00, 0x01))
DISPLAY_BITMAP = bytearray((0xc8, 0xef, 0x69, 0x00, 0x17, 0x70))

STARTMODE_DEFAULT = bytearray((0x00,))
STARTMODE_IMAGE = bytearray((0x01,))
STARTMODE_VIDEO = bytearray((0x02,))
FLIP_180 = bytearray((0x01,))
NO_FLIP = bytearray((0x00,))
SEND_PAYLOAD = bytearray((0xFF,))

# Function to pad a message to a multiple of 250 bytes with null bytes (0x00)
def pad(message):
  msg_size = len(message)
  if not (msg_size / 250).is_integer():
    pad_size = (250 * math.ceil(msg_size / 250) - msg_size)
    message += b"\x00" * pad_size
  return message

if __name__ == "__main__":
  # Open a serial connection to the device at /dev/ttyACM0 with a baud rate of 115200
  # timeout=1 sets a 1-second read timeout
  # rtscts=1 enables RTS/CTS hardware flow control
  ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1, rtscts=1)
  # Send the HELLO command padded to a multiple of 250 bytes
  ser.write(pad(HELLO))
  # Reads 22 bytes of response from the device
  resp = ser.read(22)
  # Decode and print the response from the device
  print(resp.decode())
  # Sends the SET_BRIGHTNESS command with brightness level 0x40 (64 in decimal), 
  # padded to a multiple of 250 bytes
  ser.write(pad(SET_BRIGHTNESS + b"\x40"))
  time.sleep(1)
  # Sends the SET_BRIGHTNESS command with brightness level 0x00 (0 in decimal), 
  # padded to a multiple of 250 bytes
  ser.write(pad(SET_BRIGHTNESS + b"\x00"))

