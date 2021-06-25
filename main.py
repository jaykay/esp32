
from machine import Pin, SPI
from time import sleep
import ssd1306
import dht

led = Pin(2, Pin.OUT)
dht22 = Pin(33)
hspi = SPI(1)  # sck=14 (scl), mosi=13 (sda), miso=12 (unused)
dc = Pin(4)    # data/command
rst = Pin(5)   # reset
cs = Pin(15)   # chip select, some modules do not have a pin for this
d = dht.DHT22(dht22)

display = ssd1306.SSD1306_SPI(128, 64, hspi, dc, rst, cs)

MIN_TEMP = 26.0
MAX_TEMP = 30.0


def status(temp):
  if MIN_TEMP <= temp <= MAX_TEMP:
    return "OK"
  return "NOK"



# $$$$$$$$$$$$$$$$
# ----------------
# FFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFF
# FFFFFFFFFFFFFFFF

while True:
  d.measure()
  temp = d.temperature()
  hum = d.humidity()

  tempStr = "Temp.: {}C".format(temp)
  humStr = "Humi.: {}%".format(hum)

  display.fill(0)
  display.contrast(10)
  display.invert(1)
  display.text("Status:      {}".format(status(temp)), 2, 4, 1)
  display.text(tempStr, 2, 18, 1)
  display.text(tempStr, 2, 26, 1)
  display.text(tempStr, 2, 34, 1)
  display.text(humStr, 2, 42, 1)
  display.text(humStr, 2, 50, 1)
  display.show()
  sleep(5.0)