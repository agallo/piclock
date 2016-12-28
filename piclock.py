#!/usr/bin/python


import time
import Adafruit_CharLCD as LCD


lcd = LCD.Adafruit_CharLCDPlate()
from datetime import datetime


lcd.clear()
while True:
    localnow = time.strftime("%H"+":"+"%M"+":"+"%S"+" %Z")
    utcnow = datetime.utcnow().strftime("%H"+":"+"%M"+":"+"%S"+" UTC")
    lcd.message(localnow + "\n")
    lcd.message(utcnow)
    lcd.home()
