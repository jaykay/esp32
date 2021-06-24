from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(3.0)

#   import esp32
#   print("Hall:")
#   print(esp32.hall_sensor())    # read the internal hall sensor
#   print("Temperature")
#   celsius = (esp32.raw_temperature() - 32) * 5/9
#   print(celsius)

import upip
upip.help()
upip.install(package_or_package_list, [path])